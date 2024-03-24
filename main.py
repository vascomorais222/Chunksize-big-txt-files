import os

def split_file_into_chunks(input_file, output_prefix, num_chunks):
    with open(input_file, 'r') as f:
        data = f.readlines()

    total_lines = len(data)
    lines_per_chunk = total_lines // num_chunks
    remainder = total_lines % num_chunks

    start_index = 0
    for i in range(num_chunks):
        chunk_size = lines_per_chunk + (1 if i < remainder else 0)
        end_index = start_index + chunk_size
        chunk_data = data[start_index:end_index]

        output_file = f"{output_prefix}_{i+1}.txt"
        with open(output_file, 'w') as f_out:
            f_out.writelines(chunk_data)

        start_index = end_index

    print(f"File '{input_file}' has been split into {num_chunks} chunks.")

def clean_previous_files(output_prefix):
    for filename in os.listdir('.'):
        if filename.startswith(output_prefix) and filename.endswith('.txt'):
            os.remove(filename)
            #print(f"Deleted {filename}")

if __name__ == "__main__":
    input_file = "GROUP_11_x278mm.txt"
    output_prefix = "inst_vel_278"
    num_chunks = 25  # Specify the number of chunks you want

    clean_previous_files(output_prefix)
    split_file_into_chunks(input_file, output_prefix, num_chunks)
