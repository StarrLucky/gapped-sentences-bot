import wordeli
import config as config
import send
enPhrasesDict = wordeli.dict(config.ENPH_SOURCE_DICT_PATH, config.ENPH_CURRENT_DICT_PATH, config.ENPH_USED_DICT_LIST_PATH)

def english_phrase():
    line = enPhrasesDict.get_random().replace(".","\\.").replace("-","\\-").replace("!","\\!").replace("?","\\?")
    phrase = line.rsplit(";", 1)
    message = f'`{phrase[0].strip()}` \n||{phrase[1].strip()}||'
    send.send_to_channel(message)
    return  message

def main() -> None:
    print(english_phrase())

if __name__ == '__main__':
    main()
