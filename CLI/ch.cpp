#include <iostream>
#include <sys/stat.h>
#include <cstdlib>
#include <string>
#include <fstream>

using std::cout, std::string,std::cerr, std::endl;

const string version = "Code Hub CLI Version alpha-v0.1.0";

class Initializer{
    private:
        string lang;
        string name;
    public:
        Initializer(string name,string lang){
            this->lang = lang;
            this->name = name;
        }
        void folderMaker(){
            if (mkdir(name.c_str())){
                cerr << "Error creating folder\n";
                return;
            }
        }
        void subfolderMaker(string foldername){
            string temp = name;
            temp.append("\\");
            temp.append(foldername);
            if (mkdir(temp.c_str())){
                cerr << "Error creating subfolder\n";
                return;
            }
        }
        void subfolderMaker(){
            string temp = name;
            temp.append("\\src");
            if (mkdir(temp.c_str())){
                cerr << "Error creating subfolder\n";
                return;
            }
        }
        void projectInit(char* main_name){
            std::fstream main;
            string temp = name;
            temp.append("\\src");
            if ((lang.compare("python")==0)||(lang.compare("Python")==0)){
                temp.append("\\");
                temp.append(main_name);
                temp.append(".py");
                //cout << temp;
                main.open(temp,std::ios::out);
                return;
            }
            if ((lang.compare("C++")==0)||(lang.compare("c++")==0)||(lang.compare("cpp")==0)){
                temp.append("\\");
                temp.append(main_name);
                temp.append(".cpp");
                //cout << temp;
                main.open(temp,std::ios::out);
                return;
            }
            if ((lang.compare("C")==0)||(lang.compare("c")==0)){
                temp.append("\\");
                temp.append(main_name);
                temp.append(".c");
                //cout << temp;
                main.open(temp,std::ios::out);
                return;
            }
            if ((lang.compare("Java")==0)||(lang.compare("java")==0)){
                temp.append("\\");
                temp.append(main_name);
                temp.append(".java");
                //cout << temp;
                main.open(temp,std::ios::out);
                return;
            }
            if ((lang.compare("JavaScript")==0)||(lang.compare("Javascript")==0)||(lang.compare("javascript")==0)){
                temp.append("\\");
                temp.append(main_name);
                temp.append(".js");
                //cout << temp;
                main.open(temp,std::ios::out);
                return;
            }
        }
};

void projectMaker(string projectName, string language, char* main_name);

int main(int argc, char **argv){
    if (argv[1] == NULL){
        cerr << "More arguments needed\nUse -help" << endl;
        return 1;
    }
    if (strcmp(argv[1],"-help")==0){
        cout << "-help: Shows commands\n" << "-version: Shows current version\n";
        cout << "-init <projectname> <language>: Creates a new project for the desired programming language" << endl;
    }
    if (strcmp(argv[1],"-version")==0){
        cout << version << endl;
    }
    if ((strcmp(argv[1],"-init")==0) && (argc == 5)){
        projectMaker((string)argv[2],(string)argv[3],argv[4]);
    }
}

void projectMaker(string projectName, string language, char* main_name){
    Initializer init = Initializer(projectName,language);
    init.folderMaker();
    init.subfolderMaker();
    init.projectInit(main_name);
}