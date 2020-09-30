import tweepy

from authorization_tokens import *

import random

#Option 1:
#Pick a phrase randomly from a list of phrases:
phrase_list = ["Hi my name is Sara",
               "Sara is my name",
               "I like twitter bots"]
random_number = random.randrange( len(phrase_list) )
message = phrase_list [random_number]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print("Done.")

# Option 2
# Create a sentence template with some blanks, and
# randomly pick a word from a list to fill in each blank
# word_list = ["mangoes", "peaches","grapfruits","persimmons"]
#
# string_template = "Some people think {} are good, but I like {}."
#
# random_number = random.randrange( len(word_list) )
# word1 = word_list [random_number]
# random_number = random.randrange( len(word_list) )
# word2 = word_list [random_number]
#
# message = string_template.format(word1,word2)

# Option 3:
# Randomly create a template from a list, then randomly pick words
# # from a word list, and use the words to fill in the string_template
# word_list = ["people","video games","sports","software"]
# template_list = ["If you like {}, you'll love {}",
#                  "You might think I'm a {} person, but actually I love {}"
#                  "You'd never guess it but I like {} even more than {}"]
# random_number = random.randrange( len(template_list) )
# template = template_list [random_number]
#
# random_number = random.randrange( len(word_list) )
# word1 = word_list [random_number]
#
# random_number = random.randrange( len(word_list) )
# word2 = word_list [random_number]
#
# message = template.format(word1,word2)


# Option 4:
# Basic search
# search_results = api.search(q="hate filter:safe", lang="en", tweetmode="extended")
# random_number = random.randrange( len(search_results) )
# random_tweet = search_results[random_number]
# message = random_tweet.full_text.replace ("hate","love")
#
# # Option 5
# # Reply to a randomly selected mention
# mentions = api.mentions_timeline()
# random_bumber = random.randrange(len(mentions))
# random_mention = mentions[random_number]
#
# message = "@" + random_mention.user.screen_name + "I am a bot."
#
# api.update_status(message, in_reply_to_status_id=random_mention.id)
