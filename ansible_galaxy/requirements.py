import logging
import os
import pprint

import yaml

from ansible_galaxy import yaml_persist
from ansible_galaxy.models.requirement import RequirementSpec
from ansible_galaxy.models.content_spec import ContentSpec
from ansible_galaxy.content_spec import spec_data_from_string
from ansible_galaxy.utils import yaml_parse
from ansible_galaxy.utils import content_name

log = logging.getLogger(__name__)


def load(data_or_file_object):
    requirements_data = yaml.safe_load(data_or_file_object)

    log.debug('requirements_data: %s', pprint.pformat(requirements_data))

    requirements_list = []

    for req_data_item in requirements_data:
        log.debug('req_data_item: %s', req_data_item)
        log.debug('type(req_data_item): %s', type(req_data_item))

        req_spec_data = yaml_parse.yaml_parse(req_data_item)
        log.debug('req_spec_data: %s', req_spec_data)

        # name_info = content_name.parse_content_name(data_name)
        # log.debug('data_name (after): %s', data_name)
        # log.debug('name_info: %s', name_info)

        req_spec = RequirementSpec.from_dict(req_spec_data)
        #req_spec = RequirementSpec(namespace=content_spec_data['namespace'],
        #                           name=content_spec_data['name'],
        #                           version=content_spec_data['version'],
        #                           src=content_spec_data['src'],
        #                           scm=content_spec_data['scm'])

        log.debug('req_spec: %s', req_spec)

        requirements_list.append(req_spec)

    log.debug('requirements_list: %s', requirements_list)
    return requirements_list


def from_requirement_spec_strings(requirement_spec_strings, namespace_override=None, editable=False):
    req_specs = []
    for requirement_spec_string in requirement_spec_strings:
        req_spec_data = spec_data_from_string(requirement_spec_string,
                                              namespace_override=namespace_override,
                                              editable=editable)

        log.debug('req_spec_data: %s', req_spec_data)

        req_spec = RequirementSpec.from_dict(req_spec_data)

        log.debug('req_spec: %s', req_spec)

        req_specs.append(req_spec)

    return req_specs