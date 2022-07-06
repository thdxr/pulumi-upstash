// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Upstash.Upstash
{
    public static class GetKafkaTopic
    {
        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Upstash = Pulumi.Upstash;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var kafkaTopicData = Output.Create(Upstash.GetKafkaTopic.InvokeAsync(new Upstash.GetKafkaTopicArgs
        ///         {
        ///             TopicId = resource.Upstash_kafka_topic.ExampleKafkaTopic.Topic_id,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetKafkaTopicResult> InvokeAsync(GetKafkaTopicArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetKafkaTopicResult>("upstash:index/getKafkaTopic:getKafkaTopic", args ?? new GetKafkaTopicArgs(), options.WithDefaults());

        /// <summary>
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Upstash = Pulumi.Upstash;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var kafkaTopicData = Output.Create(Upstash.GetKafkaTopic.InvokeAsync(new Upstash.GetKafkaTopicArgs
        ///         {
        ///             TopicId = resource.Upstash_kafka_topic.ExampleKafkaTopic.Topic_id,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetKafkaTopicResult> Invoke(GetKafkaTopicInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetKafkaTopicResult>("upstash:index/getKafkaTopic:getKafkaTopic", args ?? new GetKafkaTopicInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetKafkaTopicArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Unique Topic ID for requested kafka topic
        /// </summary>
        [Input("topicId", required: true)]
        public string TopicId { get; set; } = null!;

        public GetKafkaTopicArgs()
        {
        }
    }

    public sealed class GetKafkaTopicInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Unique Topic ID for requested kafka topic
        /// </summary>
        [Input("topicId", required: true)]
        public Input<string> TopicId { get; set; } = null!;

        public GetKafkaTopicInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetKafkaTopicResult
    {
        /// <summary>
        /// Cleanup policy will be used in the topic(compact or delete)
        /// </summary>
        public readonly string CleanupPolicy;
        /// <summary>
        /// Id of the cluster this topic belongs to
        /// </summary>
        public readonly string ClusterId;
        /// <summary>
        /// Creation time of the topic
        /// </summary>
        public readonly int CreationTime;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Max Message Size for the topic
        /// </summary>
        public readonly int MaxMessageSize;
        /// <summary>
        /// Whether multizone replication is enabled
        /// </summary>
        public readonly bool Multizone;
        /// <summary>
        /// Number of partitions the topic has
        /// </summary>
        public readonly int Partitions;
        /// <summary>
        /// Password to be used in authenticating to the cluster
        /// </summary>
        public readonly string Password;
        /// <summary>
        /// Region of the kafka topic. Possible values (may change) are: "eu-west-1", "us-east-1"
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// REST Endpoint of the topic
        /// </summary>
        public readonly string RestEndpoint;
        /// <summary>
        /// Max Retention Size of the topic
        /// </summary>
        public readonly int RetentionSize;
        /// <summary>
        /// Max Retention Time of the topic
        /// </summary>
        public readonly int RetentionTime;
        /// <summary>
        /// State of the topic (active or deleted)
        /// </summary>
        public readonly string State;
        /// <summary>
        /// TCP Endpoint of the topic
        /// </summary>
        public readonly string TcpEndpoint;
        /// <summary>
        /// Unique Topic ID for requested kafka topic
        /// </summary>
        public readonly string TopicId;
        /// <summary>
        /// Name of the kafka topic
        /// </summary>
        public readonly string TopicName;
        /// <summary>
        /// Username to be used in authenticating to the cluster
        /// </summary>
        public readonly string Username;

        [OutputConstructor]
        private GetKafkaTopicResult(
            string cleanupPolicy,

            string clusterId,

            int creationTime,

            string id,

            int maxMessageSize,

            bool multizone,

            int partitions,

            string password,

            string region,

            string restEndpoint,

            int retentionSize,

            int retentionTime,

            string state,

            string tcpEndpoint,

            string topicId,

            string topicName,

            string username)
        {
            CleanupPolicy = cleanupPolicy;
            ClusterId = clusterId;
            CreationTime = creationTime;
            Id = id;
            MaxMessageSize = maxMessageSize;
            Multizone = multizone;
            Partitions = partitions;
            Password = password;
            Region = region;
            RestEndpoint = restEndpoint;
            RetentionSize = retentionSize;
            RetentionTime = retentionTime;
            State = state;
            TcpEndpoint = tcpEndpoint;
            TopicId = topicId;
            TopicName = topicName;
            Username = username;
        }
    }
}