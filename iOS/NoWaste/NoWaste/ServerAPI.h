//
//  ServerAPI.h
//  Copyright (c) 2015 com.reynoldsJay. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface ServerAPI : NSObject <NSURLConnectionDataDelegate>

@property NSMutableArray *common;
@property NSMutableDictionary *inventory;

+ (ServerAPI*) getInstance;


- (NSString*)postData:(id)postJson toURL:(NSString*)url;
- (NSString*)getDataFromURL:(NSString*)url;

- (NSData*)parseJson:(NSString*)jsonString;

@end