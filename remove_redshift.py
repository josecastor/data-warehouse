import configparser
import boto3
import json

def create_clients(config):
    print('1.0 Creating a Client Redshift and IAM')
    redshift = boto3.client('redshift',
                           region_name=config['AWS']['REGION'],
                           aws_access_key_id=config['AWS']['KEY'],
                           aws_secret_access_key=config['AWS']['SECRET'])
    iam = boto3.client('iam',
                       region_name=config['AWS']['REGION'],
                       aws_access_key_id=config['AWS']['KEY'], 
                       aws_secret_access_key=config['AWS']['SECRET'])

    return redshift, iam;

def remove_redshift(config, redshift):
    print('1.1 Remove Redshift Cluster {}'.format(config['DWH']['DWH_CLUSTER_IDENTIFIER']))
    redshift.delete_cluster( ClusterIdentifier=config['DWH']['DWH_CLUSTER_IDENTIFIER'],  SkipFinalClusterSnapshot=True)

def remove_resource(config, iam):
    print('1.2 Remove Resource Cluster {}'.format(config['DWH']['DWH_CLUSTER_IDENTIFIER']))
    iam.detach_role_policy(RoleName=config['DWH']['DWH_IAM_ROLE_NAME'], PolicyArn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess")
    iam.delete_role(RoleName=config['DWH']['DWH_IAM_ROLE_NAME'])

def update_cfg():
    print('1.3 Remove data config')
    cfg = configparser.ConfigParser()
    cfg.read('dwh.cfg')
    cfg.set('CLUSTER', 'HOST', '')
    cfg.set('IAM_ROLE', 'ARN', '')
    cfg.set('AWS', 'KEY', '')
    cfg.set('AWS', 'SECRET', '')
    cfg.set('AWS', 'REGION', '')
    with open('dwh.cfg', "w") as config_file:
        cfg.write(config_file)
        
def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    c_redshift, c_iam = create_clients(config)
    remove_redshift(config, c_redshift)
    remove_resource(config, c_iam)
    update_cfg()

if __name__ == "__main__":
    main()