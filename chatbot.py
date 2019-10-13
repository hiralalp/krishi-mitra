from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")
from chatterbot.trainers import ListTrainer

conversation = [
    "What does the process of soil testing involve?",
    "Soil testing is divided into four sections - Soil Physics, Soil Chemistry and Fertility, Soil Biology and Environmental Soil Science",
    
    "How do I select the right pesticides?",
    "Information about the correct combination of fertilizers and doses for particular crops is available with your local area or block agriculture officer.",
    
    "What is the import duty for different agricultural products?",
    "Wheat grains have an import duty of 100 per cent; rice has a duty of 80 per cent while the rate for maize is 70 per cent. Grains like rye, barley, oats, buckwheat and canary seed may be imported for free. Soybeans, groundnut, linseed, sunflower seeds, cottonseeds, mustard seeds and the like have an import duty of 35 per cent. Coffee and Tea has a standard duty of 100 per cent. Spices like black pepper, cardamom, chilly and cloves have a duty rate of 70 per cent.",
    
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

response = chatbot.get_response("how to select the right pesticides")
print(response)