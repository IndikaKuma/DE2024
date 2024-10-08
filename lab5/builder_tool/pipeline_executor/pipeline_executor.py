import argparse
import json
import logging
import sys

import google.cloud.aiplatform as aip


def run_pipeline_job(name, pipeline_def, pipeline_root, parameter_dict):
    # Opening JSON file
    f = open(parameter_dict)
    data = json.load(f)
    print(data)
    logging.info(data)
    job = aip.PipelineJob(
        display_name=name,
		enable_caching=False,
        template_path=pipeline_def,
        pipeline_root=pipeline_root,
        parameter_values=data)
    job.run()


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, help="Pipeline Name")
    parser.add_argument('--pipeline_def', type=str, default="pipeline.json", help="Pipeline JSON definition file")
    parser.add_argument('--pipeline_root', type=str, help="GCP bucket for pipeline_root")
    parser.add_argument('--parameter_dict', type=str, help="Pipeline parameters as a josn file")
    args = parser.parse_args()
    return vars(args)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    run_pipeline_job(**parse_command_line_arguments())
