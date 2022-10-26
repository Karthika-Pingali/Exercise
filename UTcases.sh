#!/bin/bash

echo "Unit Test cases"
function ut1() {
    Image_tag="$(grep  "image: " /Users/karthikapingali/capk.yaml| wc -l)"
    echo "No.of image tags in original file=$Image_tag "
    Fimage_tag="$(grep  "image: " /Users/karthikapingali/final.yaml| wc -l)"
    echo "No. of image tags in output file=$Fimage_tag"
    if [ $Image_tag == $Fimage_tag ]
    then :
        echo "No Image tag is missing"
    else
        echo "Image tag is missing"
    fi
}
function ut2(){
   Image_tag1="$(grep  "imagePullPolicy: IfNotPresent" /Users/karthikapingali/capk.yaml| wc -l)"
   echo "No.of image pull policy tags=$Image_tag1"
   Fimage_tag1="$(grep  "imagePullPolicy: IfNotPresent" /Users/karthikapingali/final.yaml| wc -l)"
   echo "No.of image pull policy tags in output=$Fimage_tag1"
    if [ $Image_tag1 == $Fimage_tag1 ]
    then
       echo "No Image Pull Policy is added to original yaml file"
    else
        echo "Image Pull Ploicy is added or edited"
    fi

}
function ut3() {
   Image_tag2="$(grep  "imagePullPolicy: Always" /Users/karthikapingali/capk.yaml| wc -l)"
   echo "No.of image pull policy tags=$Image_tag2"
   Fimage_tag2="$(grep  "imagePullPolicy: Always" /Users/karthikapingali/final.yaml| wc -l)"
   echo "No.of image pull policy tags in output=$Fimage_tag2" 
   if [ $Image_tag2 == 0 ]
   then
       echo "No imagePullPolicy: Always is present in original yaml file"
    elif [ $Image_tag2 !=0 && $Fimage_tag2 ==0 ]
    then
         echo "imagePullPolicy: Always tag has been edited"
    fi
}
function ut4(){
    Image_tag3="$(grep  "imagePullPolicy: Never" /Users/karthikapingali/capk.yaml| wc -l)"
   echo "No.of image pull policy tags=$Image_tag3"
   Fimage_tag3="$(grep  "imagePullPolicy: Never" /Users/karthikapingali/final.yaml| wc -l)"
   echo "No.of image pull policy tags in output=$Fimage_tag3"
   if [ $Image_tag3 == 0 ]
   then
       echo "No imagePullPolicy: Never is present in original yaml file"
    elif [ $Image_tag2 !=0 && $Fimage_tag2 ==0 ]
    then
         echo "imagePullPolicy: Never tag has been edited"
    fi
}
ut1
ut2
ut3
ut4