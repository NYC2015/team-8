//
//  ServerAPI.m
//
//  Copyright (c) 2015 com.reynoldsJay. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "ServerAPI.h"

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



@end