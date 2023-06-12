# from feel_number import feel_numbers
#from from_two_files import name_gen
#from two_files_in_one import two_files_in_one
from two_files_in_one import two_files_in_one
from gen_files import gen_files

if __name__ == '__main__':
    # print(feel_numbers(5, 'my_file'))
    # name_gen(10, 4, 7, 'file_2.txt')
    #two_files_in_one('my_file', 'file_2.txt', 'res.txt')
    #two_files_in_one()
    gen_files('bin', 5, 10, 1024, 4096, 5)

