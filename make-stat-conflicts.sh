python get-avg.py log/ttp-midas/*-ss/ failures stats/midas-conflicts-ss.csv
python get-avg.py log/ttp-midas/*-sl/ failures stats/midas-conflicts-sl.csv
python get-avg.py log/ttp-midas/*-ls/ failures stats/midas-conflicts-ls.csv
python get-avg.py log/ttp-midas/*-ll/ failures stats/midas-conflicts-ll.csv

python get-avg.py log/ttp-midas-unlocked/*-ss/ failures stats/midas-unlocked-conflicts-ss.csv
python get-avg.py log/ttp-midas-unlocked/*-sl/ failures stats/midas-unlocked-conflicts-sl.csv
python get-avg.py log/ttp-midas-unlocked/*-ls/ failures stats/midas-unlocked-conflicts-ls.csv
python get-avg.py log/ttp-midas-unlocked/*-ll/ failures stats/midas-unlocked-conflicts-ll.csv

python get-avg.py log/ttp-echo/*-ss/ failures stats/echo-conflicts-ss.csv
python get-avg.py log/ttp-echo/*-sl/ failures stats/echo-conflicts-sl.csv
python get-avg.py log/ttp-echo/*-ls/ failures stats/echo-conflicts-ls.csv
python get-avg.py log/ttp-echo/*-ll/ failures stats/echo-conflicts-ll.csv
