def main():
    n = int(input())
    info_dict = []
    for _ in range(n):
        info_dict.append(list(map(int, input().split(" "))))
    space_list = []
    for info in info_dict :
        if not space_list :
            time_list = [0 for i in range(0, 24)]
            for i in range(info[0], info[1]) :
                time_list[i] = 1
            space_list.append(time_list)
        else :
            done = False
            temp = []
            while space_list :
                space = space_list.pop()
                empty = True
                for i in range(info[0], info[1]) :
                    if space[i] == 1 :
                        empty = False
                        break
                if empty :
                    done = True
                    for i in range(info[0], info[1]) :
                        space[i] = 1
                temp.append(space)
            space_list += temp
            if not done :
                time_list = [0 for i in range(0, 24)]
                for i in range(info[0], info[1]) :
                    time_list[i] = 1
                space_list.append(time_list)
    return len(space_list)
if __name__ == '__main__':
    print(main())