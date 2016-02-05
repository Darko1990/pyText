import sys
import os.path

if __name__ == "__main__":
    print(sys.argv[1])
    if len(sys.argv[1]) > 0:
        if os.path.isfile(sys.argv[0]):
            file = open(sys.argv[1], '+r', encoding='utf-8')
            for row in file:
                file.writelines(row.replace(" ", ", ", 1))
                print(row)
                # something new
            file.close();
    else:
        print("Enter filename")
