"""
Custom semantic segmentation handler for model archive
"""



import torch
from ts.torch_handler.base_handler import BaseHandler

import my_utils


class TestHandler(BaseHandler):
    """
    A custom model handler implementation for semantic segmentation.
    """

    def preprocess(self, data):
        """The preprocess function of MNIST program converts the input data to a float tensor

        Args:
            data (List): Input data from the request is in the form of a Tensor

        Returns:
            list : The preprocess function returns the input image as a list of float tensors.
        """
        preprocessed_images = my_utils.preprocessing()
        print("***** Doing preprocessing...")
        
        return preprocessed_images


    def inference(self, preprocessed_images):
        """
        The Inference Function is used to make a prediction call on the given input request.
        The user needs to override the inference function to customize it.

        Args:
            data (Torch Tensor): A Torch Tensor is passed to make the Inference Request.
            The shape should match the model input shape.

        Returns:
            Torch Tensor : The Predicted Torch Tensor is returned in this function.
        """
        print("***** Doing inferencing...")
        predicted_logits = 1

        return predicted_logits
    

    def postprocess(self, predicted_logits):
        """
        The post process function makes use of the output from the inference and converts into a
        Torchserve supported response output.

        Args:
            data (Torch Tensor): The torch tensor received from the prediction output of the model.

        Returns:
            List: The post process function returns a list of the predicted output.
        """
        print("***** Doing postprocessing...")
        final_prediction = predicted_logits
        return final_prediction
    

    def handle(self, data, context):
        """Entry point for default handler. It takes the data from the input request and returns
           the predicted outcome for the input.

        Args:
            data (list): The input data that needs to be made a prediction request on.
            context (Context): It is a JSON Object containing information pertaining to
                               the model artifacts parameters.

        Returns:
            list : Returns a dictionary with the predicted response.
        """
        print("***** In the handle function...")
        preprocessed_images = self.preprocess(data)
        predicted_logits = self.inference(preprocessed_images)
        final_prediction = self.postprocess(predicted_logits)
        final_result = {
            "prediction": final_prediction,
            "others": "Hello"
        }

        return [final_result]

