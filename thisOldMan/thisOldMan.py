"""
This old man, he played one,
He played knick knack with his thumb,
With a knick, knack, paddy whack,
Give the dog a bone;
This old man came rolling home.
This old man, he played two,
He played knick knack with my shoe,
With a knick, knack, paddy whack,
Give the dog a bone;
This old man came rolling home.
This old man, he played three,
He played knick knack on my knee,
With a knick, knack, paddy whack,
Give the dog a bone;
This old man came rolling home.
This old man, he played four,
He played knick knack at my door,
With a knick, knack, paddy whack,
Give the dog a bone;
This old man came rolling home.
This old man, he played five,
He played knick knack, jazz and jive,
With a knick, knack, paddy whack,
Give the dog a bone;
This old man came rolling home.
This old man, he played six,
He played knick knack with his sticks,
With a knick, knack, paddy whack,
Give the dog a bone;
This old man came rolling home.
This old man, he played seven,
He played knick knack with his pen,
With a knick, knack, paddy whack,
Give the dog a bone;
This old man came rolling home.
This old man, he played eight,
He played knick knack on my gate,
With a knick, knack, paddy whack,
Give the dog a bone;
This old man came rolling home.
This old man, he played nine,
He played knick knack, rise and shine,
With a knick, knack, paddy whack,
Give the dog a bone;
This old man came rolling home.
This old man, he played ten,
He played knick knack in my den,
With a knick, knack, paddy whack,
Give the dog a bone;
This old man came rolling home.
This old man, he played eleven,
He played knick knack up in heaven,
With a knick, knack, paddy whack,
Give the dog a bone;
This old man came rolling home.
This old man, he played twelve,
He played knick knack, dig and delve,
With a knick, knack, paddy whack,
Give the dog a bone;
This old man came rolling home.
"""

knickKnacks = [0, "with his thumb", "with my shoe", "on my knee", "at my door",
               "jazz and jive", "with his sticks", "with his pen","at my gate",
               "rise and shine", "in my den", "up in heaven", "dig and delve"]

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
          "nine", "ten", "eleven", "twelve"]

for i in range(1, 13):
    print("This old man, he played " + numbers[i] + ",\nhe played knick knack with his " + knickKnacks[i] + ',')
    print("With a knick, knack, paddy whack,\nGive the dog a bone;\nThis old man came rolling home.\n")