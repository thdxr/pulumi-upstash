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
 * const exampleQstashEndpointData = upstash.getQStashEndpoint({
 *     endpointId: resource.upstash_qstash_endpoint.exampleQstashEndpoint.endpoint_id,
 * });
 * ```
 */
export function getQStashEndpoint(args: GetQStashEndpointArgs, opts?: pulumi.InvokeOptions): Promise<GetQStashEndpointResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("upstash:index/getQStashEndpoint:getQStashEndpoint", {
        "topicId": args.topicId,
    }, opts);
}

/**
 * A collection of arguments for invoking getQStashEndpoint.
 */
export interface GetQStashEndpointArgs {
    topicId: string;
}

/**
 * A collection of values returned by getQStashEndpoint.
 */
export interface GetQStashEndpointResult {
    readonly endpointId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly topicId: string;
    readonly url: string;
}

export function getQStashEndpointOutput(args: GetQStashEndpointOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetQStashEndpointResult> {
    return pulumi.output(args).apply(a => getQStashEndpoint(a, opts))
}

/**
 * A collection of arguments for invoking getQStashEndpoint.
 */
export interface GetQStashEndpointOutputArgs {
    topicId: pulumi.Input<string>;
}