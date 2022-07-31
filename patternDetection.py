import csv

from mend import mend

def main():
    data = []

    with open('data_main.csv', 'r') as f:
        csv_reader = csv.reader(f)
        for i in csv_reader:
            data.append(i)
    
    for i in data:
        argument = i[0]
        out = i[1]

        if argument in out:
            print("correlation between arg and out")
            otherParts = []
            out_vals = out.split(" ")
            for part in out_vals:
                if argument != part:
                    otherParts.append(part)
                else:
                    arg_ind = out_vals.index(part)
        mend(otherParts,arg_ind)

if __name__ == '__main__':
    main()