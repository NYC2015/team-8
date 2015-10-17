//
//  ViewController.m
//  NoWaste
//
//  Created by Jay Reynolds on 10/17/15.
//  Copyright © 2015 com.reynoldsJay. All rights reserved.
//

#import "Common.h"
#import "ServerAPI.h"

@interface Common()

@property IBOutlet UITableView *common;


@end

@implementation Common {
    NSArray *exampleItems;
    ServerAPI *server;
    NSString *select;
}

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    server = [ServerAPI getInstance];
    exampleItems = server.common;
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

// table view methods

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView
{
    return 1;
}


- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return [exampleItems count];
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *simpleTableIdentifier = @"cell";
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:simpleTableIdentifier forIndexPath:indexPath];
    
    if (cell == nil) {
        cell = [[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:simpleTableIdentifier];
    }
    
    UILabel *cellLabel = (UILabel *)[cell viewWithTag:10];
    cellLabel.text = exampleItems[indexPath.row];
    

    
    
    
    return cell;
}

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath
{
    
    select = exampleItems[indexPath.row];
    UIAlertView *message = [[UIAlertView alloc] initWithTitle:@"Pounds:"
                                                    message:nil
                                                     delegate:self
                                            cancelButtonTitle:@"Cancel"
                                            otherButtonTitles:@"Continue", nil];
    
    [message setAlertViewStyle:UIAlertViewStylePlainTextInput];
    [message show];
    
}
- (void)alertView:(UIAlertView *)alertView clickedButtonAtIndex:(NSInteger)buttonIndex
{
    if (buttonIndex == 1) {
        server.inventory[select] = [alertView textFieldAtIndex:0].text;
        [self performSegueWithIdentifier:@"toInv" sender:self];
    }
}


@end
