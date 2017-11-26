import unittest
from gotoh2 import Aligner


class TestAligner(unittest.TestCase):
    def setUp(self):
        self.g2 = Aligner()
        self.g2.gap_open_penalty = 5

        # HXB2 is a standard HIV-1 (subtype B) reference sequence
        self.hxb2_integrase = 'TTTTTAGATGGAATAGATAAGGCCCAAGATGAACATGAGAAATATCACAGTAATTGGAGAGCAATGGCTAGTGATTTTAACCTGCC' \
                              'ACCTGTAGTAGCAAAAGAAATAGTAGCCAGCTGTGATAAATGTCAGCTAAAAGGAGAAGCCATGCATGGACAAGTAGACTGTAGTC' \
                              'CAGGAATATGGCAACTAGATTGTACACATTTAGAAGGAAAAGTTATCCTGGTAGCAGTTCATGTAGCCAGTGGATATATAGAAGCA' \
                              'GAAGTTATTCCAGCAGAAACAGGGCAGGAAACAGCATATTTTCTTTTAAAATTAGCAGGAAGATGGCCAGTAAAAACAATACATAC' \
                              'TGACAATGGCAGCAATTTCACCGGTGCTACGGTTAGGGCCGCCTGTTGGTGGGCGGGAATCAAGCAGGAATTTGGAATTCCCTACA' \
                              'ATCCCCAAAGTCAAGGAGTAGTAGAATCTATGAATAAAGAATTAAAGAAAATTATAGGACAGGTAAGAGATCAGGCTGAACATCTT' \
                              'AAGACAGCAGTACAAATGGCAGTATTCATCCACAATTTTAAAAGAAAAGGGGGGATTGGGGGGTACAGTGCAGGGGAAAGAATAGT' \
                              'AGACATAATAGCAACAGACATACAAACTAAAGAATTACAAAAACAAATTACAAAAATTCAAAATTTTCGGGTTTATTACAGGGACA' \
                              'GCAGAAATCCACTTTGGAAAGGACCAGCAAAGCTCCTCTGGAAAGGTGAAGGGGCAGTAGTAATACAAGATAATAGTGACATAAAA' \
                              'GTAGTGCCAAGAAGAAAAGCAAAGATCATTAGGGATTATGGAAAACAGATGGCAGGTGATGATTGTGTGGCAAGTAGACAGGATGA' \
                              'GGATTAG'

        # RT = reverse transcriptase
        self.hxb2_rt = 'CCCATTAGCCCTATTGAGACTGTACCAGTAAAATTAAAGCCAGGAATGGATGGCCCAAAAGTTAAACAATGGCCATTGACAGAAGAAAAAATA' \
                       'AAAGCATTAGTAGAAATTTGTACAGAGATGGAAAAGGAAGGGAAAATTTCAAAAATTGGGCCTGAAAATCCATACAATACTCCAGTATTTGCC' \
                       'ATAAAGAAAAAAGACAGTACTAAATGGAGAAAATTAGTAGATTTCAGAGAACTTAATAAGAGAACTCAAGACTTCTGGGAAGTTCAATTAGGA' \
                       'ATACCACATCCCGCAGGGTTAAAAAAGAAAAAATCAGTAACAGTACTGGATGTGGGTGATGCATATTTTTCAGTTCCCTTAGATGAAGACTTC' \
                       'AGGAAGTATACTGCATTTACCATACCTAGTATAAACAATGAGACACCAGGGATTAGATATCAGTACAATGTGCTTCCACAGGGATGGAAAGGA' \
                       'TCACCAGCAATATTCCAAAGTAGCATGACAAAAATCTTAGAGCCTTTTAGAAAACAAAATCCAGACATAGTTATCTATCAATACATGGATGAT' \
                       'TTGTATGTAGGATCTGACTTAGAAATAGGGCAGCATAGAACAAAAATAGAGGAGCTGAGACAACATCTGTTGAGGTGGGGACTTACCACACCA' \
                       'GACAAAAAACATCAGAAAGAACCTCCATTCCTTTGGATGGGTTATGAACTCCATCCTGATAAATGGACAGTACAGCCTATAGTGCTGCCAGAA' \
                       'AAAGACAGCTGGACTGTCAATGACATACAGAAGTTAGTGGGGAAATTGAATTGGGCAAGTCAGATTTACCCAGGGATTAAAGTAAGGCAATTA' \
                       'TGTAAACTCCTTAGAGGAACCAAAGCACTAACAGAAGTAATACCACTAACAGAAGAAGCAGAGCTAGAACTGGCAGAAAACAGAGAGATTCTA' \
                       'AAAGAACCAGTACATGGAGTGTATTATGACCCATCAAAAGACTTAATAGCAGAAATACAGAAGCAGGGGCAAGGCCAATGGACATATCAAATT' \
                       'TATCAAGAGCCATTTAAAAATCTGAAAACAGGAAAATATGCAAGAATGAGGGGTGCCCACACTAATGATGTAAAACAATTAACAGAGGCAGTG' \
                       'CAAAAAATAACCACAGAAAGCATAGTAATATGGGGAAAGACTCCTAAATTTAAACTGCCCATACAAAAGGAAACATGGGAAACATGGTGGACA' \
                       'GAGTATTGGCAAGCCACCTGGATTCCTGAGTGGGAGTTTGTTAATACCCCTCCCTTAGTGAAATTATGGTACCAGTTAGAGAAAGAACCCATA' \
                       'GTAGGAGCAGAAACCTTC'

        # NL4-3 is another HIV-1 reference that is commonly used in laboratory experiments - this is the sequence for the pol gene
        self.nl43 = 'TTTTTTAGGGAAGATCTGGCCTTCCCACAAGGGAAGGCCAGGGAATTTTCTTCAGAGCAGACCAGAGCCAACAGCCCCACCAGAAGAGAGCTTCAG' \
                    'GTTTGGGGAAGAGACAACAACTCCCTCTCAGAGGCAGGAGCCGATAGACAAGGAACTGTATCCTTTAGCTTCCCTCAGATCACTCTTTGGCAGCGA' \
                    'CCCCTCGTCACAATAAAGATAGGGGGGCAATTAAAGGAAGCTCTATTAGATACAGGAGCAGATGATACAGTATTAGAAGAAATGAATTTGCCAGGA' \
                    'AGATGGAAACCAAAAATGATAGGGGGAATTGGAGGTTTTATCAAAGTAAGACAGTATGATCAGATACTCATAGAAATCTGCGGACATAAAGCTATA' \
                    'GGTACAGTATTAGTAGGACCTACACCTGTCAACATAATTGGAAGAAATCTGTTGACTCAGATTGGCTGCACTTTAAATTTTCCCATTAGTCCTATT' \
                    'GAGACTGTACCAGTAAAATTAAAGCCAGGAATGGATGGCCCAAAAGTTAAACAATGGCCATTGACAGAAGAAAAAATAAAAGCATTAGTAGAAATT' \
                    'TGTACAGAAATGGAAAAGGAAGGAAAAATTTCAAAAATTGGGCCTGAAAATCCATACAATACTCCAGTATTTGCCATAAAGAAAAAAGACAGTACT' \
                    'AAATGGAGAAAATTAGTAGATTTCAGAGAACTTAATAAGAGAACTCAAGATTTCTGGGAAGTTCAATTAGGAATACCACATCCTGCAGGGTTAAAA' \
                    'CAGAAAAAATCAGTAACAGTACTGGATGTGGGCGATGCATATTTTTCAGTTCCCTTAGATAAAGACTTCAGGAAGTATACTGCATTTACCATACCT' \
                    'AGTATAAACAATGAGACACCAGGGATTAGATATCAGTACAATGTGCTTCCACAGGGATGGAAAGGATCACCAGCAATATTCCAGTGTAGCATGACA' \
                    'AAAATCTTAGAGCCTTTTAGAAAACAAAATCCAGACGTAGTCATCTATCAATACATGGATGATTTGTATGTAGGATCTGACTTAGAAATAGGGCAG' \
                    'CATAGAACAAAAATAGAGGAACTGAGACAACATCTGTTGAGGTGGGGATTTACCACACCAGACAAAAAACATCAGAAAGAACCTCCATTCCTTTGG' \
                    'ATGGGTTATGAACTCCATCCTGATAAATGGACAGTACAGCCTATAGTGCTGCCAGAAAAGGACAGCTGGACTGTCAATGACATACAGAAATTAGTG' \
                    'GGAAAATTGAATTGGGCAAGTCAGATTTATGCAGGGATTAAAGTAAGGCAATTATGTAAACTTCTTAGGGGAACCAAAGCACTAACAGAAGTAGTA' \
                    'CCACTAACAGAAGAAGCAGAGCTAGAACTGGCAGAAAACAGGGAGATTCTAAAAGAACCGGTACATGGAGTGTATTATGACCCATCAAAAGACTTA' \
                    'ATAGCAGAAATACAGAAGCAGGGGCAAGGCCAATGGACATATCAAATTTATCAAGAGCCATTTAGAAATCTGAAAACAGGAAAGTATGCAAGAATG' \
                    'AAGGGTGCCCACACTAATGATGTGAAACAATTAACAGAGGCAGTACAAAAAATAGCCACAGAAAGCATAGTAATATGGGGAAAGACTCCTAAATTT' \
                    'AAATTACCCATACAAAAGGAAACATGGGAAGCATGGTGGACAGAGTATTGGCAAGCCACCTGGATTCCTGAGTGGGAGTTTGTCAATACCCCTCCC' \
                    'TTAGTGAAGTTATGGTACCAGTTAGAGAAAGAACCCATAATAGGAGCAGAAACTTTCTATGTAGATGGGGCAGCCAATAGGGAAACTAAATTAGGA' \
                    'AAAGCAGGATATGTAACTGACAGAGGAAGACAAAAAGTTGTCCCCCTAACGGACACAACAAATCAGAAGACTGAGTTACAAGCAATTCATCTAGCT' \
                    'TTGCAGGATTCGGGATTAGAAGTAAACATAGTGACAGACTCACAATATGCATTGGGAATCATTCAAGCACAACCAGATAAGAGTGAATCAGAGTTA' \
                    'GTCAGTCAAATAATAGAGCAGTTAATAAAAAAGGAAAAAGTCTACCTGGCATGGGTACCAGCACACAAAGGAATTGGAGGAAATGAACAAGTAGAT' \
                    'AAATTGGTCAGTGCTGGAATCAGGAAAGTACTATTTTTAGATGGAATAGATAAGGCCCAAGAAGAACATGAGAAATATCACAGTAATTGGAGAGCA' \
                    'ATGGCTAGTGATTTTAACCTACCACCTGTAGTAGCAAAAGAAATAGTAGCCAGCTGTGATAAATGTCAGCTAAAAGGGGAAGCCATGCATGGACAA' \
                    'GTAGACTGTAGCCCAGGAATATGGCAGCTAGATTGTACACATTTAGAAGGAAAAGTTATCTTGGTGGCAGTTCATGTAGCCAGTGGATATATAGAA' \
                    'GCAGAAGTAATTCCAGCAGAGACAGGGCAAGAAACAGCATACTTCCTCTTAAAATTAGCAGGAAGATGGCCAGTAAAAACAGTACATACAGACAAT' \
                    'GGCAGCAATTTCACCAGTACTACAGTTAAGGCCGCCTGTTGGTGGGCGGGAATCAAGCAGGAATTTGGCATTCCCTACAATCCCCAAAGTCAAGGA' \
                    'GTAATAGAATCTATGAATAAAGAATTAAAGAAAATTATAGGACAGGTAAGAGATCAGGCTGAACATCTTAAGACAGCAGTACAAATGGCAGTATTC' \
                    'ATCCACAATTTTAAAAGAAAAGGGGGGATTGGGGGGTACAGTGCAGGGGAAAGAATAGTAGACATAATAGCAACAGACATACAAACTAAAGAATTA' \
                    'CAAAAACAAATTACAAAAATTCAAAATTTTCGGGTTTATTACAGGGACAGCAGAGATCCAGTTTGGAAAGGACCAGCAAAGCTCCTCTGGAAAGGT' \
                    'GAAGGGGCAGTAGTAATACAAGATAATAGTGACATAAAAGTAGTGCCAAGAAGAAAAGCAAAGATCATCAGGGATTATGGAAAACAGATGGCAGGT' \
                    'GATGATTGTGTGGCAAGTAGACAGGATGAGGATTAA'

        # an entire HIV-1 genome sequence
        self.u54771 = 'GGGTCTCTCTTGTTAGACCAGGTCGAGCCCGGGAGCTCTCTGGCTAGCAAGGGAACCCACTGCTTAAAGCCTCAATAAAGCTTGCCTTGAGTGC' \
                      'TTAAAGTGGTGTGTGCCCGTCTGTGTTAGGACTCTGGTAACTAGAGATCCCTCAGACCACTCTAGACTGAGTAAAAATCTCTACCAGTGGCGCC' \
                      'CGAACAGGGCACTCGAAAGCGAAAGTTAATAGGGACTCGAAAGCGAAAGTTCCAGAGAAGTTCTCTCGACGCAGGACTCGGCTTGCTGAGGTGC' \
                      'ACACAGCAAGAGGCGAGAGCGGCGACTGGTGAGTACGCCAAATTTTGACTAGCGGAGGCTAGAAGGAGAGAGATGGGTGCGAGAGCGTCAGTAT' \
                      'TAAGTGGGGGAAAATTAGATGCATGGGAAAAAATTCGGTTGCGGCCAGGGGGAAGAAAAAAATATAGGCTGAAACATTTAGTATGGGCAAGCAG' \
                      'AGAGTTAGAAAGATTCGCACTTAACCCTAGCTTTTTAGAAACAGCAGAAGGATGTCAACAAATAATAGAACAGTTACAGTCAACTCTCAAGACA' \
                      'GGATTAGAAGAACTTAAATCATTATTTAATACAGTAGCAACCCTCTGGTGCGTACACCAAAGGATAGAGGTAAAAGACACCAAGGAAGCTTTAG' \
                      'ATAAAATAGAGGAAGTACAAAATAAGAGCCAGCGAAAGACACAGCAGGCAGCAGCTGGCACAGGAAGCAGCAGCAAAGTCAGCCAAAATTACCC' \
                      'TATAGTGCAAAATGCACAAGGGCAAATGGCACATCAGCCTTTATCACCTAGAACTTTGAATGCATGGGTGAAAGTAGTAGAAGAAAAGGGTTTT' \
                      'AACCCAGAAGTAATACCCATGTTCTCAGCATTATCAGAGGGAGCCACCCCACAAGATTTAAATATGATGCTAAATATAGTGGGGGGACACCAGG' \
                      'CAGCAATGCAAATGTTAAAAGAAACCATCAATGAGGAACCTGCAGAATGGGATAGGGTACACCCAGTACATGCAGGGCCTATTCCACCAGGCCA' \
                      'GATGAGGGAACCAAGGGGAAGTGACATAGCAGGAACTACTAGTACCCTTCAAGAACAAATAGGATGGATGACAAACAATCCACCCATCCCAGTG' \
                      'GGAGACATCTATAAAAGGTGGATAATCCTGGGATTAAATAAAATAGTAAGAATGTATAGCCCTGTTAGCATTTTGGACATAAGACAAGGGCCAA' \
                      'AAGAACCCTTCAGAGACTATGTAGATAGGTTCTATAAAACTCTCAGAGCGGAACAAGCTACACAGGAGGTAAAAAACTGGATGACAGAAACCTT' \
                      'GCTAGTCCAAAACGCGAATCCAGACTGTAAGTCCATTTTAAAAGCATTAGGAACAGGAGCTACATTAGAAGAAATGATGACAGCATGCCAGGGA' \
                      'GTGGGAGGACCTAGCCATAAAGCAAGGGTTTTGGCTGAAGCAATGAGCCACGCACAACATGCAACTATAATGATGCAGAGAGGCAATTTCAAGG' \
                      'GCCAGAAAAGAATTAAGTGCTTCAACTGTGGTAGAGAAGGACACCTAGCCAGAAATTGCAGGGCCCCTAGAAAACAGGGTTGTTGGAAATGCGG' \
                      'GAAGGAAGGACATCAAATGAAAGACTGCACTGAGAGACAGGCTAATTTTTTAGGGAAAATTTGGCCTTCCAACAAGGGAAGGCCGGGGAATTTT' \
                      'CCTCAGAGCAGACCAGAGCCAACAGCCCCACCAGCAGAAAACTGGGGGATGGGGGAAGAGATAACGGGGGAAGAGATAACCTCCTTACCGAAGC' \
                      'AGGAGCAGAAAGACAAGGAACATCCTCCTCCTTTAGTTTCCCTCAAATCACTCTTTGGCAACGACCCCTTGTCACAGTAAAAATAGGAGGACAG' \
                      'CTGAAAGAAGCTCTATTAGATACAGGAGCAGATGATACAGTATTAGAAGATATAAATTTGCCAGGAAAATGGAAACCAAAAATGATAGGGGGAA' \
                      'TTGGAGGTTTTATCAAGGTAAAGCAATATGATCAGATACTTATAGAAATCTGTGGAAAAAAGGCTATAGGTACAGTATTAGTAGGACCTACACC' \
                      'TGTCAACATAATTGGACGAAATATGTTGACTCAGATTGGTTGTACTTTAAATTTCCCAATTAGTCCTATTGACACTGTACCAGTAACATTAAAG' \
                      'CCAGGAATGGATGGACCAAAGGTTAAACAGTGGCCATTGACAGAAGAAAAAATAAAAGCATTAACAGAAATTTGTAAAGAGATGGAAGAGGAAG' \
                      'GAAAAATCTCAAAAATTGGGCCTGAAAATCCATACAATACTCCAGTATTTGCTATAAAGAAAAAGGACAGCACCAAATGGAGGAAATTAGTAGA' \
                      'TTTCAGAGAGCTCAATAAAAGAACTCAGGACTTTTGGGAAGTTCAATTAGGAATACCGCATCCAGCAGGTTTAAAAAAGAAAAAATCAGTAACA' \
                      'GTACTAGATGTGGGAGATGCATATTTTTCAGTTCCTTTAGATGAAAGCTTTAGAAAGTATACTGCATTCACCATACCTAGTATAAACAATGAGA' \
                      'CACCAGGAATCAGATATCAGTACAATGTGCTGCCACAGGGATGGAAAGGATCACCGGCAATATTCCAGAGTAGCATGACAAAAATCTTAGAGCC' \
                      'CTTTAGAATAAAAAATCCAGAAATGGTTATCTATCAATACAAGGATGACTTGTATGTAGGATCTGATTTAGAAATAGGGCAGCACAGAACAAAA' \
                      'ATAGAGGAGCTAAGAGCTCATCTATTGAGCTGGGGATTTACTACACCAGACAAAAAGCATCAGAAGGAACCTCCATTCCTTTGGATGGGATATG' \
                      'AACTCCATCCTGACAGATGGACAGTCCAGCCTATAGAACTGCCAGAAAAAGACAGCTGGACTGTCAATGATATACAGAAATTAGTGGGAAAACT' \
                      'AAATTGGGCAAGTCAAATTTATGCAGGGATTAAGGTAAAGCAACTGTGTAAACTCCTCAGGGGAGCTAAAGCACTAACAGACATAGTACCACTG' \
                      'ACTGAAGAAGCAGAATTAGAGTTGGCAGAGAACAGGGAGATTCTAAAAACCCCTGTGCATGGAGTATATTATGACCCATCAAAAGACTTAGTAG' \
                      'CAGAAGTACAGAAACAAGGGCAGGACCAATGGACATATCAAATTTATCAAGAGCCATTTAAAAATCTAAAAACAGGAAAATATGCCAGAAGAGG' \
                      'GTCTGCTCACACTAATGATGTAAGACAATTAACAGAAGTGGTGCAAAAAGTAGCCACAGAAAGCATAGTAATATGGGGAAAGACCCCTAAATTT' \
                      'AGACTACCCATACAAAGAGAAACATGGGAAACATGGTGGATGGAGTATTGGCAGGCTACCTGGATTCCTGAATGGGAGTTTGTTAATACCCCTC' \
                      'CTCTAGTAAAATTATGGTACCAATTAGAAAAAGACCCCATAGTAGGAGCAGAGACTTTCTATGTAGATGGGGCAGCTAGTAGGGAGACTAAGCT' \
                      'AGGAAAAGCAGGGTATGTCACTGACAGAGGAAGACAAAAGGTAGTTTCCCTAACTGAGACAACAAATCAAAAGACTGAATTACATGCGATCCAT' \
                      'TTAGCCTTGCAGGATTCAGGATCAGAAGTAAATATAGTAACAGACTCACAATATGCATTAGGAATCATTCAGGCACAACCAGACAGGAGTGAAT' \
                      'CAGAAGTAGTCAACCAAATAATAGAGGAGCTAATAAAAAAGGAGAAAGTCTACCTGTCATGGGTACCAGCACACAAGGGGATTGGAGGAAATGA' \
                      'ACAAGTAGATAAATTAGTCAGTTCAGGAATCAGGAAGGTGCTATTTTTAGATGGGATAGATAAGGCTCAAGAAGAACATGAAAGATATCACAGC' \
                      'AATTGGAGAACAATGGCTAGTGATTTTAATTTGCCACCTATAGTAGCAAAGGAAATAGTAACCAACTGTGATAAATGTCAACTAAAAGGGGAAG' \
                      'CTATGCATGGACAAGTAGACTGTAGTCCAGGGATATGGCAATTAGATTGCACACATCTAGAAGGAAAAGTCATCCTGGTAGCAGTCCACGTGGC' \
                      'CAGTGGATATATAGAAGCAGAAGTTATCCCAGCAGAAACAGGACAGGAGACAGCATACTTTCTGCTAAAACTAGCAGGAAGATGGCCAGTAAAA' \
                      'GTAATACACACAGACAACGGTAGCAATTTCACCAGCGCTGCAGTTAAAGCAGCCTGTTGGTGGGCCAATGTCCAACAGGAATTTGGGATCCCCT' \
                      'ACAATCCCCAAAGTCAAGGAGTAGTAGAATCTATGAATAAGGAATTAAAGAAAATCATAGGGCAGGTAAGAGAGCAAGCTGAACACCTTAAAAC' \
                      'AGCAGTACAAATGGCAGTATTCATTCACAATTTTAAAAGAAAAGGGGGGATTGGGGGGTACAGTGCAGGGGAAAGAATAATAGACATAATAGCA' \
                      'ACAGACATACAAACTAAAGAATTACAAAAACAAATTACAAAAATTCAAAATTTTCGGGTTTATTACAGGGACAGCAGAGACCCAATTTGGAAAG' \
                      'GACCAGCAAAACTACTCTGGAAAGGTGAAGGGGCAGTAGTAATACAAGACAATAGTGATATAAAAGTAGTACCAAGAAGAAAAGCAAAGATCAT' \
                      'TAGGGATTATGGAAAACAGATGGCAGGTGATGATTGTGTGGCAGGTAGACAGGATGAGGATTAGAACATGGAACAGTTTAGTAAAACATCATAT' \
                      'GTATATCTCAAAGAAAGCTAAAAAGTGGTTTTATAGACATCATTATGAAAGCCAGCATCCAAAGGTAAGCTCAGAAGTACATATCCCACTAGGA' \
                      'GAGGCTAGATTAGTAATAAGAACATATTGGGGTCTGCAAACAGGAGAAAAGGACTGGCACTTGGGTCATGGAGTCTCCATAGAATGGAGGCAGA' \
                      'GAAAATATAGCACACAAATAGATCCTGACCTAGCAGACAAACTGATTCATCTACAATATTTTGGCTGTTTTTCAGACTCTGCCATAAGGAAAGC' \
                      'CATATTAGGACAAGTAGTTAGACGTAGGTGTGAATATCCATCAGGACATAACAAGGTAGGATCCCTACAATATTTGGCACTGAAAGCATTAACA' \
                      'ACACCAAAAAGGATAAGGCCACCTCTGCCTAGTGTAGAAATAACAGAAGATAGATGGAACAAGCCCCAGAAGAGGGGCCACAGAGAGAACCCTA' \
                      'CAATGAATGGACATTAGAACTGTTAGAGGAGCTTAAAAATGAAGCTGTTAGACATTTTCCTAGGCCCTGGCTCCAAGGCTTAGGACAGTACATC' \
                      'TATAACAATTATGGGGATACTTGGGAAGGGGTTGAAGCTATAATAAGAATGTTGCAACAACTACTGTTTGTTCATTTCAGAATTGGGTGTCAAC' \
                      'ATAGCAGAATAGGCATTATGCCAGGGAGAAGAGGCAGGAATGGAACTGGTAGATCCTAACCTAGAGCCCTGGAATCATCCGGGAAGTCAGCCTA' \
                      'CAACTGCTTGTAGCAAGTGTTACTGTAAAAAATGTTGCTGGCATTGCCAACTATGCTTTCTGAAAAAAGGCTTAGGCATCTCCTATGGCAGGAA' \
                      'GAAGCGGAAGCACCGACGAGGAACTCCTCAGAGCAGTAAGGATCATCAAAATCCTATACCAAAGCAGTAAGTAATAAGTATATGTAATGACACC' \
                      'TTTGGAAATTAGTGCAATAGTAGGACTGATAGTAGCGCTAATCTTAGCAATAGTAGTGTGAACTATAGTAGCTATAGAAGTTAAGAAAATACTA' \
                      'AGGCAAAGAAAAATAGACAGGTTAGTTAAGAGAATAAGAGAAAGAGCAGAAGACAGTGGAAATGAGAGTGAAGGAGACACAGATGAATTGGCCA' \
                      'AACTTGTGGAAATGGGGGACTTTGATCCTTGGGTTGGTGATAATTTGTAGTGCCTCAGACAACTTGTGGGTTACAGTTTATTATGGGGTGCCTG' \
                      'TGTGGAGAGATGCAGATACCACCCTATTTTGTGCATCAGATGCCAAGGCACATGAGACAGAAGTGCACAATGTCTGGGCCACACATGCCTGTGT' \
                      'ACCCACAGACCCCAACCCACAAGAAATACACCTGGAAAATGTAACAGAAAATTTTAACATGTGGAAAAATAACATGGTAGAGCAGATGCAGGAG' \
                      'GATGTAATCAGTTTATGGGATCAAAGTCTAAAGCCATGTGTAAAGTTAACTCCTCTCTGCGTTACTTTAAATTGTACCAATGCTAATTTGACCA' \
                      'ATGGCAGTAGCAAAACCAATGTCTCTAACATAATAGGAAATATAACAGATGAAGTAAGAAACTGTACTTTTAATATGACCACAGAACTAACAGA' \
                      'TAAGAAGCAGAAGGTCCATGCACTCTTTTATAAGCTTGATATAGTACAAATTGAAGATAAGAAGACTAGTAGTGAGTATAGGTTAATAAATTGT' \
                      'AATACTTCAGTCATTAAGCAGGCTTGTCCAAAGATATCCTTTGATCCAATTCCTATACATTATTGTACTCCAGCTGGTTATGCGATTTTAAAGT' \
                      'GTAATGATAAGAATTTCAATGGGACAGGGCCATGTAAAAATGTCAGCTCAGTACAATGCACACATGGAATTAAGCCAGTGGTATCAACTCAATT' \
                      'GCTGTTAAATGGCAGTCTAGCAGAAGAAGAGATAATAATCAGATCTGAAGATCTCACAAACAATGCCAAAACCATAATAGTGCACCTTAATAAA' \
                      'TCTGTAGAAATCAATTGTACCAGACCCTCCAACAATACAAGAACAAGTATAACTATAGGACCAGGACGAGTATTCTATAGAACAGGAGATATAA' \
                      'TAGGAAATATAAGAAAAGCATATTGTGAGATTAATGGAACAAAATGGAATAAAGTTTTAAAACAGGTAACTGAAAAATTAAAAGAGCACTTTAA' \
                      'TAAGACAATAATCTTTCAACCACCCTCAGGAGGAGATCTAGAAATTACAATGCATCATTTTAATTGTAGAGGGGAATTTTTCTATTGCAATACA' \
                      'ACAAAACTGTTTAATAATACTTGCCTAGGAAATGAAACCATGGCGGGGTGTAATGACACTATCACACTTCCATGCAAGATAAAGCAAATTATAA' \
                      'ACATGTGGCAGGGAGCAGGACAAGCAATGTATGCTCCTCCCATCAGTGGAAGAATTAATTGTGTATCAAATATTACAGGAATACTATTGACAAG' \
                      'AGATGGTGGTGTTAATAATACGGATAACGAGACCTTCAGACCTGGAGGAGGAAACATAAAGGACAATTGGAGAAGTGAATTATATAAATATAAA' \
                      'GTAGTACAAATTGAACCACTAGGAATAGCACCCACCAGGGCAAAGAGAAGAGTGGTGGAGAGAGAAAAAAGGGCAGTGGGAATAGGAGCTATGA' \
                      'TCTTTGGGTTCTTAGGAGCAGCAGGAAGCACTATGGGCGCGGCGTCAATAACGCTGACGGTACAGGCCAGACAATTATTGTCTGGTATAGTGCA' \
                      'ACAGCAAAGCAATTTGCTGAGGGCTATAGAGGCGCAGCAGCATCTGTTGCAACTCACAGTCTGGGGCATTAAACAGCTCCAGGCAAGAGTCCTG' \
                      'GCTGTGGAAAGATACCTAAAGGATCAAAAGTTCCTAGGACTTTGGGGCTGCTCTGGAAAAATCATCTGCACCACTGCTGTGCCCTGGAACTCCA' \
                      'CTTGGAGTAATAGATCTTTTGAAGAGATTTGGAACAACATGACATGGATAGAATGGGAGAGAGAAATTAGCAATTACACAAACCAAATATATGA' \
                      'GATACTTACAGAATCGCAGAACCAACAGGACAGGAATGAAAAGGATTTGTTAGAATTGGATAAATGGGCAAGTCTGTGGAATTGGTTTGACATA' \
                      'ACAAATTGGCTGTGGTATATAAAAATATTTATAATGATAGTAGGAGGTTTAATAGGTTTAAGAATAATTTTTGCTGTGCTTTCTATAGTAAATA' \
                      'GAGTTAGGCAGGGATACTCACCTTTGTCTTTCCAGACCCCTTCCCATCATCAGAAGGAACCCGACAGACCCGAAGGAATCGAAGAAGGAGGTGG' \
                      'CGAGCAAGGCAGAGACAGATCAGTGCGATTAGTGAGCGGATTCTTAGCACTTGCCTGGGACGATCTACGGAGCCTGTGCCTCTTCAGCTACCAC' \
                      'CGGTTGAGAGACTTAACCTTGATTGCAGCGAGGACGGTGGAACTTCTGGGACACAGCAGTCTCAAGGGACTGAGACGGGGGTGGGAAGGCCTCA' \
                      'AATATCTGGGGAATCTTCTGTTATATTGGGGCCAGGAACTAAAAATTAGTGCTATTTCTTTGCTTGATGCTACAGCAATAGCAGCAGCGGGGTG' \
                      'GACAGACAGGGTTATAGAAGTAGCACAAGGAGCTTGGAGAGCCATTCTCCACATACCTAGAAGAATCAGACAGGGCTTAGAAAGGACTTTGCTA' \
                      'TAACATGGGAAGTAAGTGGTCAAAAAGTAGCATAGTGGGATGGCCTCAGGTCAGGGAAAAAATAAAGCAAACTCCTCCAGCAACAGAAGGAGTA' \
                      'GGAGCAGTATCTCAAGATCTAGATAAACATGGAGCAATAACAAGTAGTAATATAGATAATGCTGATTGTGTCTGGCTGAGAGCACAAGAGGACG' \
                      'AGGAGGTAGGCTTTCCAGTCATGCCGCAGGTACCTCTAAGACCAATGACTTATAAGGGAGCTTTTGATCTTAGCTTCTTTTTAAAAGAAAAGGG' \
                      'GGGACTGGATGGGCTAATTTACTCCAAGAAAAGACAAGAGATCCTTGACTTATGGGTCTATAATACACAAGGCTTCTTCCCTGATTGGCAAAAC' \
                      'TACACACCAGGGCCAGGGATCAGATTCCCACTGTGTTTTGGATGGTGCTTCAAGCTAGTACCAGTTGACCAAAGAGAAGTAGAGGAGGACAACA' \
                      'AAGGAGAAAACAACTGCCTGTTACACCCCATGAGCCAGCATGGAATAGAGGACGAAGAAAGAGAAGTGCTGATGTGGAAGTTTGACAGTGCCCT' \
                      'AGCACGAAAACACGTAGCCCGAGAACAGCATCCAGAGTACTATAAAGACTGCTGACAAGGAAGTTTCTACTAGAACTTCCGCTGGGGACTTTCC' \
                      'AGGGGAGGTGTGGCCGGGGCGGAGTTGGGGAGTAGCTAACCCTCAGATGCTGCATAAAAGCAGCCGCTTTTCGCTTGTACTGGGTCTCTCTTGT' \
                      'TAGACCAGGTCGAGCCCGGGAGCTCTCTGGCTAGCAAGGGAACCCACTGCTTAAAGCCTCAATAAAGCTTGCCTTGAGTGCTTAA'

class TestAlignerSimpleGlobal(TestAligner):
    def runTest(self):
        aligned_ref, aligned_query, aligned_score = self.g2.align('ACGT', 'ACT')
        expected = 'ACGT'
        self.assertEqual(expected, aligned_ref)
        expected = 'AC-T'
        self.assertEqual(expected, aligned_query)
        expected = 5 + 5 + (-5 - 1) + 5  # 9
        self.assertEqual(expected, aligned_score)


class TestAlignerLongerGlobal(TestAligner):
    def runTest(self):
        aref, aquery, ascore = self.g2.align('ACGTACGTACGTACGT', 'ACGTACGTACTACGT')
        expected = 'ACGTACGTAC-TACGT'
        self.assertEqual(expected, aquery)
        # TODO: run progressively longer sequences


class TestAlignerSimpleLocal(TestAligner):
    def runTest(self):
        self.g2.is_global = False
        aligned_ref, aligned_query, aligned_score = self.g2.align('TACGTA', 'ACGT')
        expected = 'TACGTA'
        self.assertEqual(expected, aligned_ref)
        expected = '-ACGT-'
        self.assertEqual(expected, aligned_query)
        expected = 20
        self.assertEqual(expected, aligned_score)

class TestIssue5(TestAligner):
    def runTest(self):
        # this runs ok
        result = self.g2.align('ACGTT', 'ACGT')
        # this reproducibly crashes! no longer
        result = self.g2.align('ACGT', 'ACGTTTTTTTTTTTTTTTTTTTTTTTTTTTT')

class TestFlouri(TestAligner):
    """
    Evaluate test cases described in Flouri et al. bioRxiv 031500
    """

    def test_NWalign_example(self):
        self.g2.is_global = True
        self.g2.gap_open_penalty = 10
        self.g2.gap_extend_penalty = 1
        self.g2.set_model('NWALIGN')

        a1, a2, result = self.g2.align('GGTGTGA', 'TCGCGT')
        expected = -3
        self.assertEqual(expected, result)

    def test_Biopp_example1(self):
        self.g2.is_global = True
        self.g2.gap_open_penalty = 5
        self.g2.gap_extend_penalty = 1
        self.g2.set_model('Biopp')  # 0 match, -1 mismatch

        a1, a2, score = self.g2.align('AAAGGG', 'TTAAAAGGGGTT')
        expected = -15
        # there appear to be multiple solutions with same score
        self.assertEqual(expected, score)

    def test_Biopp_example2(self):
        self.g2.is_global = True
        self.g2.gap_open_penalty = 40
        self.g2.gap_extend_penalty = 1
        self.g2.set_model('Biopp2')  # +10 match, -30 mismatch
        a1, a2, score = self.g2.align('AAATTTGC', 'CGCCTTAC')


class TestIssues(TestAligner):
    def test_issue6(self):
        ref = self.hxb2_integrase[:100]
        query = self.u54771[:100]
        self.g2.is_global = True
        self.g2.gap_open_penalty = 2
        self.g2.align(ref, query)

    def test_issue5(self):
        # this runs ok
        result = self.g2.align('ACGTT', 'ACGT')
        # this reproducibly crashes!
        result = self.g2.align('ACGT', 'ACGTTTTTTTTTTTTTTTTTTTTTTTTTTTT')

    def test_issue14(self):
        #ref = 'CA'
        #query = 'A'
        self.g2.is_global = True
        self.g2.gap_open_penalty = 10
        self.g2.gap_extend_penalty = 1
        self.g2.set_model('HYPHY_NUC')
        #result = self.g2.align(ref, query)
        #expected = ('CA', '-A', -6)
        #self.assertEqual(expected, result)

        ref = 'GCA'
        query = 'CA'
        result = self.g2.align(ref, query)
        expected = ('GCA', '-CA', -1)
        self.assertEqual(expected, result)

    def test_issue15(self):
        ref = 'ERM'
        query = 'ERM'
        self.g2.is_global = False
        self.g2.set_model('EmpHIV25')
        self.g2.gap_open_penalty=40
        self.g2.gap_extend_penalty=10
        result = self.g2.align(ref, query)
        expected = ('ERM', 'ERM', 24)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
