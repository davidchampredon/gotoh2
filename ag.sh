cd $(dirname $0)

PATHSEQ="/Users/davidchampredon/Dropbox/MyStudies/_explorations/BAM-files/"
REFSEQ="ref-SARSCOV2-NC_045512.txt"
QUERYSEQ='fasta/EPI_ISL_425231.fasta'
OUTFILE='out-gotoh2-gisaid.txt'

echo $QUERYSEQ
echo $REFSEQ

python3 gotoh2.py $PATHSEQ$QUERYSEQ $PATHSEQ$REFSEQ > $OUTFILE

cp $OUTFILE $PATHSEQ$OUTFILE

echo "--> Alignment of GISAID seq done."

