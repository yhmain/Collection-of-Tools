# Collection-of-Tools  
# Usage:
I developed some visualization tools for analyzing password data sets.  
Project Structures:

tool_file.py Functions that store some file operations.  
tool_plot.py A function that plots data.  

Tool1:  
tool_character.py Analyze the frequency of each character in the file content, and draw pictures in descending order of frequency.

1.If you want to use it, please import tool_file.py and tool_plot.py.  
2.The result is shown in figure  

![image](https://github.com/yhmain/Collection-of-Tools/blob/main/Pictures/characters.png)  

Tool2:  
soft_keyboard.py 
1. generate a virtual keyboard   
2. display the input password track on the keyboard  
3. The result is shown in figure   
    
![image](https://github.com/yhmain/Collection-of-Tools/blob/main/Pictures/keyboard.png)

Sample input: password 'zxcvbn2345tgb'  

Tool3:  
tool_wordcloud.py  
1.Read a data set and draw word cloud according to word frequency display.
![image](https://github.com/yhmain/Collection-of-Tools/blob/main/Pictures/wordcloud.png)

Tool4:  
digit_analysi.py  
1.Analyze the situation of password protected digit string in password dataset.

Tool5:  
special_analysis.py  
1.Analyze the situation of password protected Special and Upper Letter string in password dataset.

Tool6:
tool_topN.py  Take out the top N passwords in the data set.  
1.If you want to use it, please import tool_file.py  
2.The result is shown in figure  
![image](https://github.com/yhmain/Collection-of-Tools/blob/main/Pictures/topN.png)

Tool7:
tool_pwd_key_pattern.py  
1.Analyze the keyboard mode of a password  
2.Four kinds of returned results: 'NO_PATTERN', 'SAME_ROW', 'ZIG_ZAG', 'SNAKE'  
3.The result is shown in figure  
![image](https://github.com/yhmain/Collection-of-Tools/blob/main/Pictures/keyPattern.png)
