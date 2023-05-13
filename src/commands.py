from time import sleep
import discord
from discord.ext import commands
from src.questions import Scopes, random_question_id
from src.queries import Query, Mutation
from src.util import translate_sentiment
from src.errors import APIResponseErrors


client = commands.Bot(
    intents=discord.Intents.all(),
    command_prefix='//'
)

 
@client.event
async def on_ready():
    print("READY!")


@client.command()
async def ping(ctx):
    await ctx.send('pong')


@client.command(aliases=['s1'])
async def scope1(ctx):
    questions = Query.query_scope_questions(Scopes.SCOPE_1.value)
    answers = {i['id']: {'answer': None, 'sentiment': None} for i in questions} 

    created_answers = []

    for question in questions:
        await ctx.send(question['question'])
        answer = await client.wait_for('message')
        answers[question['id']]['answer'] = answer
        
        await ctx.send("Você se sentiu bem ou ou mal?")
        sentiment = await client.wait_for('message')
        sentiment = translate_sentiment(sentiment.content)
        answers[question['id']]['sentiment'] = sentiment

        data = {
            'id': question['id'],
            'answer': answer.content,
            'username': ctx.author.name,
            'user_id': ctx.author.id,
            'sentiment': sentiment
        }
        response = Mutation.create_answer(data)
        created_answers.append(response['data'])
        sleep(1.5)

    await ctx.send(response)


@client.command(aliases=['rq', 'rd', 'random', 'rdm'])
async def random_question(ctx):
    """
    Random pick a NA question.
    Remember to be honest and sincere on your answer! <3
    """
    # random select a question ID and query it from backend
    question = Query.query_question_by_id(random_question_id())

    # Send question to Discord chat
    await ctx.send(question['question'])

    # Wait for the user to answer with text message
    answer = await client.wait_for('message')

    # Ask user if he feels good or bad
    await ctx.send("Você se sentiu bem ou ou mal?")
    sentiment = await client.wait_for('message')

    # Convert user sentiment response to boolean
    sentiment = translate_sentiment(sentiment.content)

    # Structure the collected data and sends to backend
    data = {
        'id': question['id'],
        'answer': answer.content,
        'username': ctx.author.name,
        'user_id': ctx.author.id,
        'sentiment': sentiment
    }
    response = Mutation.create_answer(data)

    # Ensure the API response has the answer field, otherwise inform the user
    if 'answer' not in response.keys():
        return await ctx.send(APIResponseErrors.ANSWER_CREATE)

    # Returns a beauty embeded response
    embed = discord.Embed(color=0x1E1E1E, type='rich')
    embed.add_field(name='Resposta: ', value=response['answer']['textAnswer'], inline=False)
    embed.add_field(name='Data: ', value=response['answer']['datetime'], inline=False)
    return await ctx.send('Registrado', embed=embed)


# TODO ask a number of question to randomly return

# TODO randomly ask the lesser answered question