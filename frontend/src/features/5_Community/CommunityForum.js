// Placeholder UI for the Community Q&A feature.

import React from 'react';
import { VStack, Heading, Text, Divider, HStack, Avatar, Tag } from '@chakra-ui/react';

const ForumPost = ({ name, tag, question }) => (
  <VStack align="start" w="100%" bg="white" p={4} borderRadius="md" borderWidth={1}> 
    <HStack justify="space-between" w="100%">
      <HStack>
        <Avatar size="sm" name={name} />
        <Text fontWeight="bold">{name}</Text>
      </HStack>
      <Tag size="sm" colorScheme="blue">{tag}</Tag>
    </HStack>
    <Text>{question}</Text>
  </VStack>
);

const CommunityForum = () => {
  return (
    <VStack
      w="100%"
      borderWidth={1}
      borderRadius="lg"
      boxShadow="lg"
      bg="gray.50"
      p={6}
      spacing={4}
      align="stretch"
    >
      <Heading size="lg" textAlign="center">Community Q&A</Heading>
      <Text textAlign="center" color="gray.500">Feature coming soon!</Text>
      <Divider />
      <ForumPost 
        name="Anonymous User" 
        tag="MYSY Scheme" 
        question="Did anyone else have trouble getting the income certificate online? What was the process?" 
      />
      <ForumPost 
        name="Anonymous User" 
        tag="PM-KISAN" 
        question="My eKYC failed. Where should I go in Vadodara to get it fixed?" 
      />
    </VStack>
  );
};

export default CommunityForum;