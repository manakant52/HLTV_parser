from bs4 import BeautifulSoup


open_part = ">#"
end_part = "<"
count = 1

final_part = open_part + str(count)+ end_part
print(final_part)

with open('code.txt', "r") as file_open:
    file_content = file_open.read()

    while count<31:
        open_part = ">#"
        end_part = "<"
        final_part = open_part + str(count)+ end_part
        if final_part in file_content:
            index = file_content.index(final_part)
            new_content = file_content[index: index+63]
            with open('results.txt', 'a') as file:
                file.write(new_content)
        int(count)
        count+=1

content = ''

with open('results.txt', 'r') as file:
    while True:
        char = file.read(1)
        if not char:
            break
        content += char

soup = BeautifulSoup(content, 'html.parser')

teams = soup.find_all('img')

for team in teams:
    team_name = team['alt']
    print(team_name)
