// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as pulumi from "@upstash/pulumi";
 *
 * // Not necessary if the topic belongs to an already created cluster.
 * const exampleKafkaCluster = new upstash.KafkaCluster("exampleKafkaCluster", {
 *     clusterName: "Terraform_Upstash_Cluster",
 *     region: "eu-west-1",
 *     multizone: false,
 * });
 * const exampleKafkaTopic = new upstash.KafkaTopic("exampleKafkaTopic", {
 *     topicName: "TerraformTopic",
 *     partitions: 1,
 *     retentionTime: 625135,
 *     retentionSize: 725124,
 *     maxMessageSize: 829213,
 *     cleanupPolicy: "delete",
 *     clusterId: resource.upstash_kafka_cluster.exampleKafkaCluster.cluster_id,
 * });
 * const exampleKafkaConnector = new upstash.KafkaConnector("exampleKafkaConnector", {
 *     clusterId: exampleKafkaCluster.clusterId,
 *     properties: {
 *         collection: "user123",
 *         "connection.uri": "mongodb+srv://test:test@cluster0.fohyg7p.mongodb.net/?retryWrites=true&w=majority",
 *         "connector.class": "com.mongodb.kafka.connect.MongoSourceConnector",
 *         database: "myshinynewdb2",
 *         topics: exampleKafkaTopic.topicName,
 *     },
 * });
 * // OPTIONAL: change between restart-running-paused
 * // running_state = "running"
 * ```
 */
export class KafkaConnector extends pulumi.CustomResource {
    /**
     * Get an existing KafkaConnector resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KafkaConnectorState, opts?: pulumi.CustomResourceOptions): KafkaConnector {
        return new KafkaConnector(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'upstash:index/kafkaConnector:KafkaConnector';

    /**
     * Returns true if the given object is an instance of KafkaConnector.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is KafkaConnector {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === KafkaConnector.__pulumiType;
    }

    /**
     * Name of the connector
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * Unique Connector ID for created connector
     */
    public /*out*/ readonly connectorId!: pulumi.Output<string>;
    /**
     * Creation of the connector
     */
    public /*out*/ readonly creationTime!: pulumi.Output<number>;
    /**
     * Name of the connector
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Properties that the connector will have
     */
    public readonly properties!: pulumi.Output<{[key: string]: any}>;
    /**
     * Running state of the connector. Can be either 'paused', 'running' or 'restart'
     */
    public readonly runningState!: pulumi.Output<string | undefined>;

    /**
     * Create a KafkaConnector resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: KafkaConnectorArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: KafkaConnectorArgs | KafkaConnectorState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as KafkaConnectorState | undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["connectorId"] = state ? state.connectorId : undefined;
            resourceInputs["creationTime"] = state ? state.creationTime : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["properties"] = state ? state.properties : undefined;
            resourceInputs["runningState"] = state ? state.runningState : undefined;
        } else {
            const args = argsOrState as KafkaConnectorArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.properties === undefined) && !opts.urn) {
                throw new Error("Missing required property 'properties'");
            }
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["properties"] = args ? args.properties : undefined;
            resourceInputs["runningState"] = args ? args.runningState : undefined;
            resourceInputs["connectorId"] = undefined /*out*/;
            resourceInputs["creationTime"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(KafkaConnector.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering KafkaConnector resources.
 */
export interface KafkaConnectorState {
    /**
     * Name of the connector
     */
    clusterId?: pulumi.Input<string>;
    /**
     * Unique Connector ID for created connector
     */
    connectorId?: pulumi.Input<string>;
    /**
     * Creation of the connector
     */
    creationTime?: pulumi.Input<number>;
    /**
     * Name of the connector
     */
    name?: pulumi.Input<string>;
    /**
     * Properties that the connector will have
     */
    properties?: pulumi.Input<{[key: string]: any}>;
    /**
     * Running state of the connector. Can be either 'paused', 'running' or 'restart'
     */
    runningState?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a KafkaConnector resource.
 */
export interface KafkaConnectorArgs {
    /**
     * Name of the connector
     */
    clusterId: pulumi.Input<string>;
    /**
     * Name of the connector
     */
    name?: pulumi.Input<string>;
    /**
     * Properties that the connector will have
     */
    properties: pulumi.Input<{[key: string]: any}>;
    /**
     * Running state of the connector. Can be either 'paused', 'running' or 'restart'
     */
    runningState?: pulumi.Input<string>;
}
