from itertools import permutations, product, combinations_with_replacement
import argparse

class Dimensions():
    def __init__(self, number_of_layers, input_hight, input_width, output_hight, output_width, vstride=None, hstride=None, kernel=False):
        self.number_of_layers = number_of_layers
        self.input_hight = input_hight
        self.input_width = input_width
        #self.input_chennals = input_channels
        self.output_hight = output_hight
        self.output_width = output_width
        #self.output_chennals = output_channels
        
        if vstride == None and hstride == None:
            self.strides = list(permutations(range(1,10), 2))
            
        elif vstride == None and hstride != None:
            s = [range(1,10), [hstride]]
            self.strides = [p for p in product(*s)]
            
        elif vstride != None and hstride == None:
            s = [[vstride],range(1,10)]
            self.strides = [p for p in product(*s)]
            
        else:
            self.strides = [(vstride, hstride)]
            
        if kernel == True:
            self.kernel_sizes = [(p, p) for p in range(1,10)]
            
        else:    
            self.kernel_sizes = list(permutations(range(1,10), 2))
        self.padding = ['VALID', 'SAME']
		
    def layer(self, i_hight, i_width, kernel_sizes, strides, padding='VALID'):
        if padding == 'VALID':
            H = ((i_hight - kernel_sizes[0]) /strides[0]) + 1
            W = ((i_width - kernel_sizes[1]) /strides[1]) + 1
        else:
                
            if i_hight % strides[0] == 0:
                pad_along_height = max((kernel_sizes[0] - strides[0]), 0)
            else:
                pad_along_height = max(kernel_sizes[0] - (i_hight % strides[0]), 0)
            if i_width % strides[1] == 0:
                pad_along_width = max((kernel_sizes[1] - strides[1]), 0)
            else:
                pad_along_width = max(kernel_sizes[1] - (i_width % strides[1]), 0)
                
            H = ((i_hight - kernel_sizes[0] + pad_along_height) /strides[0]) + 1
            W = ((i_width - kernel_sizes[1] + pad_along_width) /strides[1]) + 1  
        
        return H, W

    def maxpool2d(self, height, width):
        return int(height/2), int(width/2)
    
    
    def get_dim(self):
        result = []
        height = self.input_hight
        width = self.input_width
        ksp = [self.kernel_sizes, self.strides, self.padding]
        ksp = [c for c in product(*ksp)]
        #print(ksp)
        ksp = ( b for b in combinations_with_replacement(ksp, self.number_of_layers))
        for k in ksp:
            
            #print(k)
            for l, kk in zip(range(self.number_of_layers), k):
                #print(f"height is {height} and width is {width}")
                #print(kk)
                height, width = self.layer(height, width, kk[0], kk[1], kk[2])
                height, width = self.maxpool2d(height, width)
                
                #print(kk)
            #print(f"height is {height} and width is {width}")    
                
            if height == self.output_hight and width == self.output_width:
                 #print(k)
                 result.append(k)
             
            height = self.input_hight
            width = self.input_width   
        if len(result) > 0:
            return result
        return "No MATCH FOUND!!!"
            
        
if __name__ == "__main__":

            
            parser = argparse.ArgumentParser(description= "THIS SCRIPT IS USEFUL TO GET KERNEL SIZE, STRIDES AND PADDING FOR EACH CONV LAYER IN CONVOLUTION NETWORK TO GET DESIER OUTPUT SHAPE FROM A GIVEN INPUT IMAGE SHAPE" )
            parser.add_argument('-l', type=int, required=True, metavar='integer_value', help="Number of convolution layers in your network(only integer values accepted)")
            parser.add_argument('-ih', type=int, required=True, metavar='integer_value', help="Height of input image (only integer values accepted)")
            parser.add_argument('-iw', type=int, required=True, metavar='integer_value', help="Width of input image (only integer values accepted)")
            parser.add_argument('-oh', type=int, required=True, metavar='integer_value', help="Height of output image (only integer values accepted)")
            parser.add_argument('-ow', type=int, required=True, metavar='integer_value', help="Width of output image (only integer values accepted)")
            parser.add_argument('-vs', type=int, default=None, metavar='integer_value', help="(optional)vertical stride for image (only integer values accepted)")
            parser.add_argument('-hs', type=int, default=None, metavar='integer_value', help="(optional)horizontal stride for image (only integer values accepted)")
            parser.add_argument('-k', type=bool, default=False, metavar='True/False', help="set True if you only want to try kernels with equal height and width (False is by default)")
            args = parser.parse_args()
            
            n_layers = args.l
            input_height = args.ih
            input_width = args.iw
            output_height = args.oh
            output_width = args.ow
            vstride = args.vs
            hstride = args.hs
            kernel = args.k
            dim = Dimensions(n_layers, input_height, input_width, output_height, output_width, vstride, hstride, kernel)
            res = dim.get_dim()
            
            for i in res:
                print(f"kernel shape, strides and padding for every convolution layer in network are {i}")
                
           
            