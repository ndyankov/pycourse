import os
import json
from filesystem import File as _File
from filesystem import Dir as _Dir
import datetime


class File(_File):
    
    @property
    def name(self):
        return self.data

    @property
    def content(self):
        with open(self.name) as f:
            text = f.read()
        return text

    @property
    def size(self):
        # TODO: homework
        pass

    @property
    def timestamp(self):
        t = os.stat(self.name).st_ctime
        return datetime.datetime.fromtimestamp(t)


class JSONFile(File):

    @property
    def content(self):
        raw_content = super(JSONFile, self).content
        return json.loads(raw_content)


class Dir(_Dir):

    def ls(self):
        result = []
        for name in os.listdir(self.data):
            fullname = os.path.join(self.data, name)

            if os.path.isfile(fullname):
                if fullname.endswith('.json'):
                    result.append(JSONFile(fullname))
                else:
                    result.append(File(fullname))

            elif os.path.isdir(fullname):
                result.append(Dir(fullname))

            else:
                # TODO: support links
                pass

        return result


class Explorer(object):

    def __init__(self, root="."):
        self.root = Dir(root)


def main():
    explorer = Explorer(".")
    directory = explorer.root
    content = directory.ls()
    print(content)
    for x in content:
        print(x)

    print('--------')
    # print content of first file
    for x in content:
        if isinstance(x, JSONFile):
            print(x.name)
            print(x.timestamp)
            data = x.content
            print(type(data))

            print(data['firstName'], data['lastName'])
            break


if __name__ == "__main__":
    main()
