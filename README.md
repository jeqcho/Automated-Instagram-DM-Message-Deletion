# Automated Instagram DM Message Deletion
In response to the spread of malicious links through Instagram DMs, this repository aims to help you clean and purge your Instagram inbox out of any malicious links you sent. They look like:

> This took me about 2 hours to make. I hope you like it.
> `http://socialbox3136.buzz/username`

> This took me about 3 hours to make. I hope you like it,
> `http://giftstore512.buzz/username`

> This took me a few hours to make. I hope you love it,
> `http://instaexpress8008.buzz/username`

The numbers 3136, 512 and 8008 can be different according to user.

Some call this the "Hours to make" scam.

This repository uses Selenium to delete the links that you have sent.

## Features
Automated deletion of a specified link sent via Instagram DMs. Supports any link. Auto scroll and allows user intervention by scrolling to the relevant targets.

## Installation
Install Selenium and required packages

`pip install -r requirements.txt`


## How to use
1. Run the program

`python main.py`

2. Set the malicious domain keyword. Since the domain might change according to user, specify only the common phrase (eg socialbox/giftstore/instaexpress)

`Enter malicious domain keyword: socialbox`

3. Login Instagram as usual.

4. Program will navigate to chats automatically.

5. Once the chats have been loaded, scroll to the users affected and press enter at the terminal to resume the program.

6. Automated scrolling is in place, so you can know be hands-free. At any point of the program, you can scroll the user list to ensure all users have their links deleted. 

## Notes
The program selects the next user to process right below the top bar, and scrolls automatically after it finishes processing the current user. If you would like to skip any users, just scroll until the next desired user is under the top bar.

## Contribution
Pull requests welcome

## License
MIT