//
//  ServerAPI.m
//
//  Copyright (c) 2015 com.reynoldsJay. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "ServerAPI.h"
#import "Config.h"

@implementation ServerAPI

@synthesize common;
@synthesize inventory;

static ServerAPI *singletonInstance;

+ (ServerAPI*)getInstance {
    if (singletonInstance == nil) {
        singletonInstance = [[super alloc] init];
    }
    return singletonInstance;
}



// returns string of json object response
- (NSString*)postData:(id)postJson toURL:(NSString*)url {
    
    //// NSLog(@"TRYING POST");
    NSError *error;
    NSData *postData = [NSJSONSerialization dataWithJSONObject:postJson options:0 error:&error];
    NSString *postLength = [NSString stringWithFormat:@"%lu",(unsigned long)[postData length]];
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    NSString *toURL = [NSString stringWithFormat:@"%@%@", @hostDomain, url];
    // NSLog(@"post %@ to %@", postJson, toURL);
    [request setURL:[NSURL URLWithString:toURL]];
    [request setHTTPMethod:@"POST"];
    [request setValue:postLength forHTTPHeaderField:@"Content-Length"];
    [request setValue:@"application/json" forHTTPHeaderField:@"Content-Type"];
    [request setHTTPBody:postData];
    
    
    NSData* responseData = nil;
    NSURLResponse* response;
    responseData = [NSMutableData data];
    error = nil;
    responseData = [NSURLConnection sendSynchronousRequest:request returningResponse:&response error:&error];
    NSString *responseString = [[NSString alloc] initWithData:responseData encoding:NSUTF8StringEncoding];
    //// NSLog(@"Response from server:%@",responseString);
    return responseString;
}

// returns string of json object response
- (NSString*)getDataFromURL:(NSString*)url {
    
    //// NSLog(@"TRYING GET");
    NSError *error;
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    [request setURL:[NSURL URLWithString:([NSString stringWithFormat:@"%@%@", @hostDomain, url])]];
    [request setHTTPMethod:@"GET"];
    [request setValue:@"application/json" forHTTPHeaderField:@"Content-Type"];
    
    
    
    NSData* responseData = nil;
    NSURLResponse* response;
    responseData = [NSMutableData data];
    error = nil;
    responseData = [NSURLConnection sendSynchronousRequest:request returningResponse:&response error:&error];
    NSString *responseString = [[NSString alloc] initWithData:responseData encoding:NSUTF8StringEncoding];
    //// NSLog(@"Response from server:%@",responseString);
    return responseString;
}

- (id)parseJson:(NSString*)jsonString {
    NSData *jsonData = [jsonString dataUsingEncoding:NSUTF8StringEncoding];
    id json = [NSJSONSerialization JSONObjectWithData:jsonData options:0 error:nil];
    return json;
}


@end