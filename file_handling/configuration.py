import io
from configparser import SafeConfigParser

def configparser_program(filename):
    parser = SafeConfigParser(inline_comment_prefixes = ('#'))
    parser.optionxform = str
    
    parser.read(filename)
    main_conf_dict = {}
    
    for section in parser.sections():
        main_conf_dict[section] = {}
        for item, value in parser.items(section):
            main_conf_dict[section][item] = value

    return main_conf_dict

def my_configuration(filename):
    if type(filename) == str and filename != '':
        df = io.FileIO(filename)

        if df != None:
            main_conf_dict, seperators = {}, [b"=",b":"]
            
            while True:
                line = df.readline()

                if line == b'':
                    break

                # recognise section
                if line.find(b"[") != -1 and line.find(b"]") != -1:
                    section_name = line[line.find(b"[")+1:line.find(b"]")]
                    main_conf_dict[section_name] = {}

                # find the settings
                for x in seperators:
                    seperator = line.find(x)

                    # find seperator
                    if seperator != -1:
                        comment = line.find(b"#")

                        # if there is comment in the settings line
                        if comment != -1:
                            line = line[:comment]
                        
                        # if not empty
                        if line != b'':
                            value = line[seperator+1:-1].strip(b' ')
                            item = line[:seperator].strip(b' ')
                            main_conf_dict[section_name][item] = value

                        break

            return main_conf_dict

def main():
    print("The configuration dictionary is: ", my_configuration("audio.conf"), "\n")
    print("Using configparser module: ", configparser_program("audio.conf"))

if __name__ == "__main__":
    main()