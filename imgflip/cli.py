import getpass

from imgflip.utils import ResponseImage, get_memes, caption_image


def main():
    memes = get_memes()
    for i, meme in enumerate(memes):
        print(i, meme['name'], meme['id'])

    index = int(input('Select id: '))
    template_id = memes[index]['id']
    username = input('Username: ')
    password = getpass.getpass()
    text0 = input('Text 0: ')
    text1 = input('Text 1: ')
    data = caption_image(template_id, username, password, text0, text1)
    print(data)
    image = ResponseImage(data['data']['url'])

    image.webbrowser()


if __name__ == '__main__':
    main()
