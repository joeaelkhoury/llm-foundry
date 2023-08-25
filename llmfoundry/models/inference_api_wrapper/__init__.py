# Copyright 2022 MosaicML LLM Foundry authors
# SPDX-License-Identifier: Apache-2.0

from llmfoundry.models.inference_api_wrapper.interface import \
    InferenceAPIEvalWrapper
from llmfoundry.models.inference_api_wrapper.trtllm import TRTLLMEvalWrapper

__all__ = ['InferenceAPIEvalWrapper', 'TRTLLMEvalWrapper']
