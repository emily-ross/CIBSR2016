#!/usr/bin/env python
import sys

def blur_array(raw_input, pre_blur, post_blur):
    output = []

    for idx in range(len(raw_input)):
        window_start = idx - post_blur
        window_end = idx + pre_blur + 1
        if window_start < 0: window_start = 0
        if window_end > len(raw_input): window_end = len(raw_input)
        output += [any(raw_input[window_start:window_end])]
    return output

def main():
    with open(sys.argv[1]) as input_file:
        raw_input = [int(i) for i in input_file]
    
    output = blur_array(raw_input, 1, 2)

    with open('fixed_file', 'w') as output_file:
        output_file.writelines(['1\n' if i else '0\n' for i in output])


if __name__ == '__main__':
    main()
