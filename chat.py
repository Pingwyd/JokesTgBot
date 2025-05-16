import os
import random
from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

# List of jokes
jokes = ["Why don’t skeletons fight each other? They don’t have the guts. 💀🥊",
    "I only know 25 letters of the alphabet. I don't know y. 🔤🤔",
    "Why did the tomato turn red? Because it saw the salad dressing. 🍅👗",
    "Why do cows wear bells? Because their horns don’t work. 🐄🔔",
    "Why did the old man fall into the well? Because he couldn’t see that well. 👴🕳️",
    "What do you call fake spaghetti? An impasta. 🍝🎭",
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾🏆",
    "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25. 🎃🎄💻",
    "Why don’t seagulls fly over the bay? Because then they’d be bagels. 🐦🥯",
    "I'm reading a book about anti-gravity. It's impossible to put down! 📚🚀",
    "There are 10 types of people in the world: those who understand binary and those who don’t. 🔢🤖",
    "How do you catch a squirrel? Climb a tree and act like a nut! 🐿️🌳",
    "Why did the bicycle fall over? It was two-tired. 🚲😴",
    "What’s a dog’s favorite instrument? The trom-bone. 🐶🎺",
    "I would tell you a UDP joke, but you might not get it. 📡😅",
    "Why did the programmer quit his job? Because he didn’t get arrays. 🧑‍💻😓",
    "Why do Java developers wear glasses? Because they don’t see sharp. ☕👓",
    "What do you get when you cross a sheep and a kangaroo? A woolly jumper. 🐑🦘",
    "Parallel lines have so much in common. It’s a shame they’ll never meet. ➖➖😢",
    "Why don’t graveyards ever get overcrowded? People are dying to get in. ⚰️💀",
    "Why did the tomato turn red? Because it saw the salad dressing. 🍅👗",
    "Why don’t oysters donate to charity? Because they’re shellfish. 🦪😜",
    "Why did the coffee file a police report? It got mugged. ☕🚓",
    "Why did the chicken go to the séance? To talk to the other side. 🐔👻",
    "I told my wife she should embrace her mistakes. She gave me a hug. 🤗❤️",
    "Why don’t crabs give to charity? Because they’re shellfish. 🦀💸",
    "What do you call fake spaghetti? An impasta. 🍝🎭",
    "Why did the bicycle fall over? It was two-tired. 🚲😴",
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾🏆",
    "Why don’t skeletons fight each other? They don’t have the guts. 💀🥊",
    "Why do cows wear bells? Because their horns don’t work. 🐄🔔",
    "How do you organize a space party? You planet. 🪐🎉",
    "What do you call cheese that isn't yours? Nacho cheese. 🧀😆",
    "Why did the banana go to the doctor? It wasn’t peeling well. 🍌🏥",
    "Why can’t you hear a pterodactyl go to the bathroom? Because the 'P' is silent. 🦖🚽",
    "What do you call an alligator in a vest? An investigator. 🐊🕵️‍♂️",
    "What do you call a snowman with a six-pack? An abdominal snowman. ⛄💪",
    "Why was the math lecture so long? The professor kept going off on a tangent. 📐😴",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one. ⛳👖",
    "Why did the cookie go to the hospital? Because he felt crummy. 🍪🏥",
    "Why don’t teddy bears ever order dessert? They’re always stuffed. 🧸🍰",
    "Why did the orange stop? It ran out of juice. 🍊⛔",
    "What do you call a belt made of watches? A waist of time. ⌚😄",
    "Why don’t elephants use computers? They’re afraid of the mouse. 🐘🖱️",
    "Why don’t pancakes tell jokes? They’d flip out. 🥞😂",
    "Why did the teddy bear say no to dessert? Because she was stuffed. 🧸🍰",
    "Why was Cinderella so bad at soccer? Because she kept running away from the ball. 👸⚽",
    "Why did the duck go to jail? He was selling quack. 🦆🚓",
    "Why can’t pirates learn the alphabet? Because they always get stuck at C. 🏴‍☠️📚",
    "How does a scientist freshen her breath? With experi-mints. 🧪🌿",
    "Why did the music teacher go to jail? Because she got caught with too many sharp objects. 🎵🔪",
    "What did the traffic light say to the car? Don’t look, I’m changing. 🚦🚗",
    "Why did the shoe go to school? To become a sneaker. 👟🏫",
    "Why did the ghost go to therapy? He had too much boo baggage. 👻🛋️",
    "What happens to a frog’s car when it breaks down? It gets toad away. 🐸🚗",
    "Why did the man put his money in the freezer? He wanted cold hard cash. 💵❄️",
    "What did one hat say to the other? 'Stay here, I'm going on ahead.' 🎩👒",
    "Why do bees have sticky hair? Because they use honeycombs. 🐝🍯",
    "What did the ocean say to the beach? Nothing, it just waved. 🌊👋",
    "Why did the student eat his homework? Because the teacher said it was a piece of cake. 📚🍰",
    "Why did the cat sit on the computer? To keep an eye on the mouse. 🐱🖱️",
    "Why don’t eggs tell jokes? They’d crack each other up. 🥚😂",
    "I told my wife she was drawing her eyebrows too high. She looked surprised. 😲👁️",
    "Why can’t your nose be 12 inches long? Because then it would be a foot. 👃🦶",
    "Why don’t skeletons ever go trick or treating? Because they have no body to go with. 💀🍬",
    "I invented a new word! Plagiarism. 📝😅",
    "I used to be addicted to soap, but I’m clean now. 🧼🚿",
    "Why was the broom late? It swept in. 🧹⌚",
    "How does a penguin build its house? Igloos it together. 🐧🏠",
    "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them. ➖😨",
    "What do you call a can opener that doesn’t work? A can’t opener. 🥫🙅‍♂️",
    "Why don’t some couples go to the gym? Because some relationships don’t work out. ❤️🏋️‍♀️",
    "What do you call a factory that makes okay products? A satisfactory. 🏭👍",
    "What did the janitor say when he jumped out of the closet? 'Supplies!' 🧹😲",
    "I'm on a seafood diet. I see food and I eat it. 🐟🍴", "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾🏆",
    "Why don't skeletons fight each other? They don't have the guts. 💀",
    "I'm reading a book about anti-gravity. It's impossible to put down! 📚🚀",
    "Why did the bicycle fall over? Because it was two-tired! 🚲",
    "What do you call a bear with no teeth? A gummy bear! 🐻",
    "Why did the tomato turn red? Because it saw the salad dressing! 🍅",
    "How do you organize a space party? You planet! 🪐🎉",
    "What do you call a fake noodle? An impasta! 🍝",
    "Why don't scientists trust atoms? Because they make up everything! ⚛️",
    "Why did the math book look sad? Because it had too many problems. ➕➖",
    "What do you call a fish with no eyes? Fsh! 🐟",
    "Why did the computer go to therapy? It had too many bytes of information to process! 💻🧠",
    "Why did the scarecrow become a successful therapist? Because he was outstanding in his field! 🌾🧠",
    "Why did the cookie go to the hospital? Because it felt crummy! 🍪🏥",
    "What do you call a lazy kangaroo? A pouch potato! 🦘",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one! ⛳👖",
    "What do you call an alligator in a vest? An investigator! 🐊🕵️‍♂️",
    "How do you organize a space party? You planet! 🪐🎉",
    "Why did the stadium get hot after the game? All the fans left! 🏟️",
    "What did the left eye say to the right eye? Between you and me, something smells! 👀",
    "What do you call a bear with no teeth? A gummy bear! 🐻",
    "Why was the math book sad? It had too many problems! ➕➖",
    "What do you call a fake noodle? An impasta! 🍝",
    "Why don't seagulls fly over the bay? Because then they'd be called bagels! 🥯",
    "How do you make a tissue dance? You put a little boogie in it! 🤧🎶",
    "What did one wall say to the other wall? 'I'll meet you at the corner!' 🧱",
    "Why did the scarecrow become a successful musician? Because he had great 'straw-nge' talent! 🌾🎵",
    "Why did the bicycle fall over? Because it was two-tired! 🚲",
    "What do you call a bear that's stuck in the rain? A drizzly bear! 🐻🌧️",
    "Why did the computer keep freezing? It left its Windows open! ❄️💻",
    "What do you call a bear with no ears? B! 🐻",
    "Why was the math book sad? Because it had too many problems. ➕➖",
    "What do you call a fake noodle? An impasta! 🍝",
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾🏆",
    "What do you call a snowman with a six-pack? An abdominal snowman! ⛄💪",
    "How do you organize a space party? You planet! 🪐🎉",
    "Why did the bicycle fall over? Because it was two-tired! 🚲",
    "What do you call a bear with no teeth? A gummy bear! 🐻",
    "Why don't skeletons fight each other? They don't have the guts. 💀",
    "I'm reading a book about anti-gravity. It's impossible to put down! 📚🚀",
    "Why did the bicycle fall over? Because it was two-tired! 🚲",
    "What do you call a bear with no teeth? A gummy bear! 🐻",
    "Why did the tomato turn red? Because it saw the salad dressing! 🍅",
    "How do you organize a space party? You planet! 🪐🎉",
    "What do you call a fake noodle? An impasta! 🍝",
    "Why don't scientists trust atoms? Because they make up everything! ⚛️",
    "Why did the math book look sad? Because it had too many problems. ➕➖",
    "What do you call a fish with no eyes? Fsh! 🐟",
    "Why did the computer go to therapy? It had too many bytes of information to process! 💻🧠",
    "Why did the scarecrow become a successful therapist? Because he was outstanding in his field! 🌾🧠",
    "Why did the cookie go to the hospital? Because it felt crummy! 🍪🏥",
    "What do you call a lazy kangaroo? A pouch potato! 🦘",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one! ⛳👖",
    "What do you call an alligator in a vest? An investigator! 🐊🕵️‍♂️",
    "How do you organize a space party? You planet! 🪐🎉",
    "Why did the stadium get hot after the game? All the fans left! 🏟️",
    "What did the left eye say to the right eye? Between you and me, something smells! 👀",
    "What do you call a bear with no teeth? A gummy bear! 🐻",
    "Why was the math book sad? It had too many problems! ➕➖",
    "What do you call a fake noodle? An impasta! 🍝",
    "Why don't seagulls fly over the bay? Because then they'd be called bagels! 🥯",
    "How do you make a tissue dance? You put a little boogie in it! 🤧🎶",
    "What did one wall say to the other wall? 'I'll meet you at the corner!' 🧱",
    "Why did the scarecrow become a successful musician? Because he had great 'straw-nge' talent! 🌾🎵",
    "Why did the bicycle fall over? Because it was two-tired! 🚲",
    "What do you call a bear that's stuck in the rain? A drizzly bear! 🐻🌧️",
    "Why did the computer keep freezing? It left its Windows open! ❄️💻",
    "What do you call a bear with no ears? B! 🐻",
    "Why was the math book sad? Because it had too many problems. ➕➖",
    "What do you call a fake noodle? An impasta! 🍝",
    "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾🏆",
    "What do you call a snowman with a six-pack? An abdominal snowman! ⛄💪",
    "How do you organize a space party? You planet! 🪐🎉",
    "Why did the bicycle fall over? Because it was two-tired! 🚲",
    "What do you call a bear with no teeth? A gummy bear! 🐻",
    "Why don't skeletons fight each other? They don't have the guts. 💀",
    "I'm reading a book about anti-gravity. It's impossible to put down! 📚🚀",
    "Why did the bicycle fall over? Because it was two-tired! 🚲",
    "What do you call a bear with no teeth? A gummy bear! 🐻",
    "Why did the tomato turn red? Because it saw the salad dressing! 🍅",
    "How do you organize a space party? You planet! 🪐🎉",
    "What do you call a fake noodle? An impasta! 🍝",
    "Why don't scientists trust atoms? Because they make up everything! ⚛️",
    "Why did the math book look sad? Because it had too many problems. ➕➖",
    "What do you call a fish with no eyes? Fsh! 🐟",
    "Why did the computer go to therapy? It had too many bytes of information to process! 💻🧠",
    "Why did the scarecrow become a successful therapist? Because he was outstanding in his field! 🌾🧠",
    "Why did the cookie go to the hospital? Because it felt crummy! 🍪🏥",
    "What do you call a lazy kangaroo? A pouch potato! 🦘",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one! ⛳👖",
    "What do you call an alligator in a vest? An investigator! 🐊🕵️‍♂️",
    "How do you organize a space party? You planet! 🪐🎉",
    "Why did the stadium get hot after the game? All the fans left! 🏟️",
    "What did the left eye say to the right eye? Between you and me, something smells! 👀",
    "What do you call a bear with no teeth? A gummy bear! 🐻",
    "Why was the math book sad? It had too many problems! ➕➖",
    "What do you call a fake noodle? An impasta! 🍝",
    "Why don't seagulls fly over the bay? Because then they'd be called bagels! 🥯",
    "How do you make a tissue dance? You put a little boogie in it! 🤧🎶",
    "What did one wall say to the other wall? 'I'll meet you at the corner!' 🧱",
    "Why did the scarecrow become a successful musician? Because he had great 'straw-nge' talent! 🌾🎵",
    "Why did the bicycle fall over? Because it was two-tired! 🚲",
    "What do you call a bear that's stuck in the rain? A drizzly bear! 🐻🌧️",
    "Why did the computer keep freezing? It left its Windows open! ❄️💻",
    "What do you call a bear with no ears? B! 🐻",
    "Why was the math book sad? Because it had too many problems."]

# Send a random joke on /jokes command
async def joking(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = random.choice(jokes)
    await update.message.reply_text(joke)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global subscribed_chat_id
    subscribed_chat_id = update.effective_chat.id

    keyboard = [
        ["/joke"],
        ["/help"],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    welcome_message = (
        "Welcome! 🤖\n"
        "You'll get a random joke every day!\n"
        "Use the buttons below to interact 👇"
    )

    await update.message.reply_text(welcome_message, reply_markup=reply_markup)


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     welcome_message = (
#         "Welcome!\n"
#         "This is a Jokes Bot 🤖\n"
#         "Enjoy your daily dose of humor!"
#     )
#     await update.message.reply_text(welcome_message)

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/jokes - Get a random joke\n"
        "/help - Show this help message"
    )
    await update.message.reply_text(help_message)

# Bot main
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("joke", joking))

    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
