# No To Hate
Project submitted for Helix Hacks 2021
Winner of the Most Technologically Advanced Award
# Inspiration

After seeing and knowing people who have been affected by hate speech on social media platforms, we decided to block hate speech before it can even be posted on social media. With the recent influx of anti-Asian American incidents and messages, we wanted to give back to the community. Our tool can help block discriminatory, racist, misogynistic, etc sentiments and make the internet a better place.

# What it does

NoToHate takes an input of a tweet or post and checks the sentiment of the input. With the sentiment of the input, NoToHate classifies the input as hate speech or not. NoToHate also censors profanity and slurs to further diminish hate speech spread on social media.

# How we built it

We built NoToHate by using Tensorflow to create and train our custom model on a dataset of tweets labeled normal or hate speech. Then we used Flask to connect the backend (ML) part of our model to the HTML/CSS pages that we created so the final project is a functional website.

# Challenges we ran into

Initially, we had trouble in getting our model to make accurate predictions. This was probably because the data we used was heavily biased towards hateful tweets, with relatively little normal tweets. This resulted in the model classifying nearly everything we entered as hateful. We then searched for more balanced datasets, and optimized our model to yield high accuracy.

# Accomplishments that we're proud of

We’re proud of our project overall. Specifically, we’re proud of our machine learning model. We taught ourselves the basics of NLP with Tensorflow in a few hours, and actually had results to show for it.

# What we learned

We learned the basics of NLP and how to perform sentiment analysis. We also gained more perspective on the problem of hate speech online. We knew that it was a problem, but our research shows that it is a large problem in our society having many detrimental consequences.

# What's next for No To Hate

In the future, we plan to expand upon our project by making a web-extension with more features to make it more accessible. We could possibly make a page censor that, when installed, automatically censors any hateful messages or swear words on the page. Alternatively, we could add web-scraping capabilities, ensuring that the user can censor a message without clicking it so they don’t have to subject themselves to its profanity.
