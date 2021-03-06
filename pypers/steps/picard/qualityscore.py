import re
from pypers.core.step import CmdLineStep

class QualityScore(CmdLineStep):
    spec = {
        "version": "1.119",
        "descr": [
            "Chart quality score distributions in a SAM or BAM file"
        ],
        "args":
        {
            "inputs": [
                {
                    "name"     : "input_files",
                    "type"     : "file",
                    "iterable" : True,
                    "descr"    : "the input sam/bam file",
                }
            ],
            "outputs": [
                {
                    "name"  : "output_stats",
                    "type"  : "file",
                    "value" : "{{input_files}}.MeanQualityByCycle.txt",
                    "descr" : "output text file containing the statistics",
                },
                {
                    "name"  : "output_pdfs",
                    "type"  : "file",
                    "value" : "{{input_files}}.QualityScoreDistribution.pdf",
                    "descr" : "output pdf file containing the score distribution chart",
                }
            ],
            "params": [
                {
                    "name"  : "validation_stringency",
                    "type"  : "enum",
                    'options' : [ 'STRICT', 'LENIENT', 'SILENT'],
                    "value" : "LENIENT",
                    "descr" : "validation stringency. Possible values: {STRICT, LENIENT, SILENT}"
                },
                {
                    "name"  : "reference",
                    "type"  : "str",
                    "descr" : "reference sequence file",
                    "value" : "null"
                },
                {
                    "name"  : "aligned_only",
                    "type"  : "boolean",
                    "descr" : "calculate mean quality over aligned reads only",
                    "value" : "True"
                },
                {
                    "name"  : "jvm_args",
                    "value" : "-Xmx{{jvm_memory}}g -Djava.io.tmpdir={{output_dir}}",
                    "descr" : "java virtual machine arguments",
                    "readonly" : True
                }
            ]
        },
        "cmd": [
            "/usr/bin/java {{jvm_args}} ",
            "-jar /software/pypers/picard-tools/picard-tools-1.119/picard-tools-1.119/QualityScoreDistribution.jar",
            " I={{input_files}} R={{reference}} O={{output_stats}} CHART={{output_pdfs}}",
            " VALIDATION_STRINGENCY={{validation_stringency}} ALIGNED_READS_ONLY={{aligned_only}}"
        ],  
        "requirements": { 
            "memory" : "8"
        },
        "extra_env" : {
            "PATH" : "/software/pypers/R/R-3.0.0/bin",
            "LD_LIBRARY_PATH": "/software/pypers/gcc/gcc-4.7.1/lib64:/software/pypers/intel/l_ics-2013.0.028/composer_xe_2013.1.117/compiler/lib/intel64"
        }
    }
