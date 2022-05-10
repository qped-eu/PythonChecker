# write the answer to a source file
echo "$answer" > ./src/answer.py

#run flake8
flake8 ./src/answer.py --output-file=output.txt

# run the analysis
python3 src/main.py
