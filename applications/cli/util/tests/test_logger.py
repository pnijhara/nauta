#
# INTEL CONFIDENTIAL
# Copyright (c) 2018 Intel Corporation
#
# The source code contained or described herein and all documents related to
# the source code ("Material") are owned by Intel Corporation or its suppliers
# or licensors. Title to the Material remains with Intel Corporation or its
# suppliers and licensors. The Material contains trade secrets and proprietary
# and confidential information of Intel or its suppliers and licensors. The
# Material is protected by worldwide copyright and trade secret laws and treaty
# provisions. No part of the Material may be used, copied, reproduced, modified,
# published, uploaded, posted, transmitted, distributed, or disclosed in any way
# without Intel's prior express written permission.
#
# No license under any patent, copyright, trade secret or other intellectual
# property right is granted to or conferred upon you by disclosure or delivery
# of the Materials, either expressly, by implication, inducement, estoppel or
# otherwise. Any license under such intellectual property rights must be express
# and approved by Intel in writing.
#

import logging

import pytest

import util.logger as logger


def test_initialize_logger():
    mock_package_name = 'mock_package'
    default_log_level = logging.DEBUG
    default_stream_handler_log_level = logging.CRITICAL

    mock_logger = logger.initialize_logger(mock_package_name)

    assert mock_logger
    assert logging.getLogger(mock_package_name).getEffectiveLevel() == default_log_level
    assert logger.STREAM_HANDLER.level == default_stream_handler_log_level


@pytest.mark.parametrize('mock_verbosity,expected_log_level', [(0, logging.CRITICAL), (1, logging.INFO),
                                                               (2, logging.DEBUG), (5, logging.DEBUG)])
def test_set_verbosity_level(mock_verbosity, expected_log_level):
    logger.set_verbosity_level(mock_verbosity)
    assert logger.get_verbosity_level() == expected_log_level