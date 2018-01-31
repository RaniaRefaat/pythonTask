num1=0;
num2=0;
def calcArea(shap,num1,num2):
    if (shap=="t"):
        result=(0.5*int(num1)*int(num2))
        return(result)

    elif (shap=="r"):        
        result=(int(num1)*int(num2))
        return(result)

    elif (shap=="s"):
        num2=num1       
        result=(int(num1)*int(num2))
        return(result) 

    elif (shap=="c"):        
        result=(3.14*(int(num1)**2))
        return(result)
    else:
        return("enter correct shap (t || r || s || c)")    

