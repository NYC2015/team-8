//
//  ViewController.h
//  NoWaste
//
//  Created by Jay Reynolds on 10/17/15.
//  Copyright © 2015 com.reynoldsJay. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface Camera : UIViewController <UIImagePickerControllerDelegate, UINavigationControllerDelegate>

@property (strong, nonatomic) IBOutlet UIImageView *imageView;

- (IBAction)takePhoto:  (UIButton *)sender;
- (IBAction)selectPhoto:(UIButton *)sender;


@end

