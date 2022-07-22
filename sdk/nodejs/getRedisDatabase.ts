// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as upstash from "@pulumi/upstash";
 *
 * const exampleDBData = upstash.getRedisDatabase({
 *     databaseId: resource.upstash_redis_database.exampleDB.database_id,
 * });
 * ```
 */
export function getRedisDatabase(args: GetRedisDatabaseArgs, opts?: pulumi.InvokeOptions): Promise<GetRedisDatabaseResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("upstash:index/getRedisDatabase:getRedisDatabase", {
        "databaseId": args.databaseId,
    }, opts);
}

/**
 * A collection of arguments for invoking getRedisDatabase.
 */
export interface GetRedisDatabaseArgs {
    databaseId: string;
}

/**
 * A collection of values returned by getRedisDatabase.
 */
export interface GetRedisDatabaseResult {
    /**
     * @deprecated Consistent option is deprecated.
     */
    readonly consistent: boolean;
    readonly creationTime: number;
    readonly databaseId: string;
    readonly databaseName: string;
    readonly databaseType: string;
    readonly dbDailyBandwidthLimit: number;
    readonly dbDiskThreshold: number;
    readonly dbMaxClients: number;
    readonly dbMaxCommandsPerSecond: number;
    readonly dbMaxEntrySize: number;
    readonly dbMaxRequestSize: number;
    readonly dbMemoryThreshold: number;
    readonly endpoint: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly multizone: boolean;
    readonly password: string;
    readonly port: number;
    readonly readOnlyRestToken: string;
    readonly region: string;
    readonly restToken: string;
    readonly state: string;
    readonly tls: boolean;
    readonly userEmail: string;
}

export function getRedisDatabaseOutput(args: GetRedisDatabaseOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetRedisDatabaseResult> {
    return pulumi.output(args).apply(a => getRedisDatabase(a, opts))
}

/**
 * A collection of arguments for invoking getRedisDatabase.
 */
export interface GetRedisDatabaseOutputArgs {
    databaseId: pulumi.Input<string>;
}
