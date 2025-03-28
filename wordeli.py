import random
import os
from git_repo import GitRepo


class FileBase:
    ln = 0

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read(self):
        raise NotImplementedError("NotImplementedError.")

    def write(self, content: str):
        raise NotImplementedError("NotImplementedError.")


class LocalFile(FileBase):
    ln = 0

    def read(self):
        temp_dict = [""]
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Файл {self.file_path} не найден.")

        f = open(self.file_path, "r")
        for ln in f:
            self.ln += 1
            temp_dict.append(ln)
        f.close()
        return temp_dict

    def write(self, content: []):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Файл {self.file_path} не найден.")
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.truncate(0)
            for ln in content:
                f.write(ln)
        f.close()


class RemoteGitHubFile(FileBase):
    ln = 0

    def __init__(self, file_path: str, repo):
        super().__init__(file_path)
        self.file_path = file_path
        self.repo = repo

    def read(self):
        content = self.repo.get_contents(self.file_path).decoded_content.decode('utf-8')
        tmp = str.split(content, "\n")
        self.ln = len(tmp)
        return tmp

    def write(self, content: []):
        self.repo.update_file(self.file_path, "Update file", "\n".join(content),
                              self.repo.get_contents(self.file_path).sha)


class dict():
    index = 0

    def __init__(self, source_file, current_file, used_file) -> None:
        # self.source_file =     LocalFile(source_file)
        # self.current_file =     LocalFile(current_file)
        # self.used_file =     LocalFile(used_file)

        repo = GitRepo().init()
        self.source_file = RemoteGitHubFile(file_path=source_file, repo=repo)
        self.current_file = RemoteGitHubFile(file_path=current_file, repo=repo)
        self.used_file = RemoteGitHubFile(file_path=used_file, repo=repo)

        self.source_dict = self.source_file.read()
        self.current_dict = self.current_file.read()
        self.used_dict = self.used_file.read()

        if self.current_file.ln <= 2:
            print("Copied source dict")
            self.current_file.write(self.source_dict)
            self.current_dict = self.source_dict

    def get_random(self):
        self.index = random.randint(0, len(self.current_dict) - 1)
        phrase = self.current_dict.pop(self.index)
        self.current_file.write(self.current_dict)
        self.used_dict.append(phrase)
        self.used_file.write(self.used_dict)
        return phrase

# newWord = dict(config.ENPH_SOURCE_DICT_PATH, config.ENPH_CURRENT_DICT_PATH, config.ENPH_USED_DICT_LIST_PATH)
# print(newWord.get_random())
