## Intro

When applying for a visa, we need to upload photos. Some visa application systems have very strict requirements on photo size (under 240KB), and using online tools like iLoveIMG often doesn’t work because the compressed images may contain compression artifacts, which can be detected and rejected by the system.

You can use this Python script to compress your photo without introducing compression artifacts, allowing it to pass the visa uploader's checks.

## How to use
1. Install dependencies
```shell
pip install pillow
```

2. Change the input_path, output path and output_size according to the requirement. 

3. Run the script