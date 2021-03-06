import os
import glob
from pypers.core.step import CmdLineStep


class Vep(CmdLineStep):
    spec = {
        "name": "Vep",
        "version": "2.3-9",
        "descr": [
            "Runs Variant Effect,",
            "from recal and tranches files pre-generated by VariantRecalibrator"
        ],
        "args":
        {
            "inputs": [
                {
                    "name"  : "input_file",
                    "type"  : "file",
                    "descr" : "input vcf file"
                }
            ],
            "outputs": [
                {
                    "name"  : "output_file",
                    "type"  : "file",
                    "value" : "{{input_file}}.csq.vcf",
                    "descr" : "variant effect output file",
                }
            ],
            "params" : [
                {
                    'name'  : 'perl_include_lib',
                    'type'  : 'str',
                    'value' : '/software/pypers/ensembl_vep/variant_effect_predictor-ensembl-71',
                    'descr' : 'the perl lib used',
                    'readonly' : True
                },
                {
                    'name'  : 'vep_script',
                    'type'  : 'str',
                    'value' : '/software/pypers/ensembl_vep/variant_effect_predictor-ensembl-71/bin/variant_effect_predictor.pl',
                    'descr' : 'Path to the vep script',
                    'readonly' : True
                },
                {
                    'name'  : 'species',
                    'type'  : 'str',
                    'value' : 'homo_sapiens',
                    'descr' : 'the species params'
                },
                {
                    'name'  : 'terms',
                    'type'  : 'str',
                    'value' : 'so',
                    'descr' : 'the terms parasms'
                },
                {
                    'name'  : 'cache_dir',
                    'type'  : 'str',
                    'value' : '/Public_data/VEP_Cache/VEP-ensembl-71/',
                    'descr' : 'the chache dir',
                    'readonly' : True
                },
                {
                    'name'  : 'extra_params',
                    'type'  : 'str',
                    'value' : '--everything --maf_1kg',
                    'descr' : 'the terms parasms',
                    'readonly' : True
                }
            ]
        },
        "cmd": [
            "perl -I {{perl_include_lib}} {{vep_script}} ",
            "--input_file {{input_file}} --species {{species}} --terms {{terms}}",
            "--vcf --output_file {{output_file}} --offline --dir {{cache_dir}}",
            "--html --force_overwrite {{extra_params}}"
        ]
    }

    def process(self):
        self.submit_cmd(self.render())
        if not os.path.exists(self.output_file):
            raise Exception("Output file not existing: %s" %self.output_file)
        else:
            self.log.info("Step %s successfully completed" % self.name)
