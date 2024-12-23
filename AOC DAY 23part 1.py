import numpy as np

# Define the file name based on the condition
FILE_NAME = "/content/day23.txt"

# Creates a list of all t computers and their connections
# Goes through the list checking each possible pair of connections to see if they are connected

def main():
    with open(FILE_NAME, "r") as f:
        # connectionMatrix[i][j] = 1 if the computers represented by i and j are connected
        connectionMatrix = np.zeros((26*26, 26*26), dtype=int)

        # list of connections to computers starting with t
        tLists = np.zeros((26, 26*26), dtype=int)
        tListLengths = np.zeros(26, dtype=int)

        for line in f:
            label1, label2 = line.strip().split('-')
            index1 = 26 * (ord(label1[0]) - ord('a')) + (ord(label1[1]) - ord('a'))
            index2 = 26 * (ord(label2[0]) - ord('a')) + (ord(label2[1]) - ord('a'))
            connectionMatrix[index1][index2] = 1
            connectionMatrix[index2][index1] = 1
            if label1[0] == 't':
                tLists[index1 % 26][tListLengths[index1 % 26]] = index2
                tListLengths[index1 % 26] += 1
            if label2[0] == 't':
                tLists[index2 % 26][tListLengths[index2 % 26]] = index1
                tListLengths[index2 % 26] += 1

        # count (and print) all t computers and networks of three containing them
        count = 0
        for i in range(26):
            for j in range(int(tListLengths[i])):
                for k in range(j + 1, int(tListLengths[i])):
                    index1 = tLists[i][j]
                    index2 = tLists[i][k]
                    # prevent double count if there is a t computer in the list
                    if index1 // 26 == ord('t') - ord('a') and index1 % 26 < i:
                        continue
                    if index2 // 26 == ord('t') - ord('a') and index2 % 26 < i:
                        continue
                    if connectionMatrix[index1][index2]:
                        print(f"t{chr(i + ord('a'))}: ", end="")
                        print(f"{chr(index1 // 26 + ord('a'))}{chr(index1 % 26 + ord('a'))}, ", end="")
                        print(f"{chr(index2 // 26 + ord('a'))}{chr(index2 % 26 + ord('a'))}")

                        count += 1

        print(count)

if __name__ == "__main__":
    main()

