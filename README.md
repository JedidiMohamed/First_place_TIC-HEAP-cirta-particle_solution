### TIC-HEAP Cirta Particle Classification Challenge
This challenge aimed to predict which type of particle is present in 10x10 images. The images are collected using detectors in the collider following many events ( collisions ).
    the metric for this challenge is : Log Loss
And this is a description of our classification solution that achieved **first** place with a score of 1.521101146 on private leaderboard.

###### Final solution :

The final solution which we used to reach such a score was a fine-tuned Catboost Classifier. We used an ensemble of catboosts each train on a different portion of the data for some classes ( the majority ones ).

###### Approach :
The main problem in this challenge was the class imbalance. You can quickly notice that there are 3 dominant classes with tens of thousands of samples, while 2 classes were having over 1300 samples and the other one around 3k samples. It is also mentioned that the test set was made to be balanced. If you train a model with the data as it is, your model will be predicting the majority classes only due to the severe class imbalance.

**Data Preprocessing** : the images' pixels were flattened and stacked in a dataframe, and each column represented a single pixel, and each row represented an image. We then were able to use sklearn and boosting algorithms on the newly created tabular data to perform classification. 

**1st approach** : Oversampling

The oversampling approach didn't yield good results since there were not too many samples in the minority classes to be able to match the number of samples in the majority classes.

**2nd approach** : Undersampling

By undersampling all the classes to 1300 samples ( equal to least populated class ) , you get a score of 1.56 with a default catboost classifier. It is a good score compared to what people achieved back then, but there was another way to improve that score a lot more. Undersampling to the 2nd least populated class. Setting the data to 3k samples per class except for the 1k3 one yielded much better results. A default classifier with this approach yielded a 1.535 score.

**Conclusion** : 1300 samples weren't enough for the other 4 classes to be well classified by the model. Setting the undersampling threshold to 3k helped the model classify these 4 classes better than the first approach, but you definitely lose some power in predicting the least populated class.
