import sys
import argparse

def split_file(input_file, output_prefix, lines_per_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    total_lines = len(lines)
    num_files = total_lines // lines_per_file

    for i in range(num_files):
        output_file = f"{output_prefix}_{i + 1}.txt"
        start_idx = i * lines_per_file
        end_idx = start_idx + lines_per_file

        with open(output_file, 'w') as f:
            f.writelines(lines[start_idx:end_idx])

    if total_lines % lines_per_file != 0:
        output_file = f"{output_prefix}_{num_files + 1}.txt"
        with open(output_file, 'w') as f:
            f.writelines(lines[num_files * lines_per_file:])

def main():
    banner = r'''
                      ██ ██   ██                     ██        
         ██████  ░██░░   ░██                    ░██        
  ██████░██░░░██ ░██ ██ ██████   ██   ██ ██████ ░██  ██████
 ██░░░░ ░██  ░██ ░██░██░░░██░   ░██  ░██░░██░░█ ░██ ██░░░░ 
░░█████ ░██████  ░██░██  ░██    ░██  ░██ ░██ ░  ░██░░█████ 
 ░░░░░██░██░░░   ░██░██  ░██    ░██  ░██ ░██    ░██ ░░░░░██
 ██████ ░██      ███░██  ░░██   ░░██████░███    ███ ██████ 
░░░░░░  ░░      ░░░ ░░    ░░     ░░░░░░ ░░░    ░░░ ░░░░░░  

    '''
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input_file", type=str, default="input_file",help="输入文件")
    parser.add_argument("-o","--output", type=str, default="output_file",help="输出文件 默认 output_file_.txt后缀")
    parser.add_argument("-l","--lines_per_file", type=int, default="400",help="每行文件个数,默认400行")
    
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
        
    input_file = args.input_file
    output_file = args.output
    lines_per_file = args.lines_per_file
    
    print(banner)
    print(input_file,output_file,lines_per_file)
    
    split_file(input_file, output_file, lines_per_file)
    
    print("分解完成!!!")
    
    

if __name__ == "__main__":
    
    main()
