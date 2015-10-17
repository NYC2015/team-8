//
//  ServerAPI.h
//  Copyright (c) 2015 com.reynoldsJay. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface ServerAPI : NSObject <NSURLConnectionDataDelegate>

@property NSMutableArray *common;
@property NSMutableDictionary *inventory;

+ (ServerAPI*) getInstance;


@end