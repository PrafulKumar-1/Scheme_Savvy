// A visually impressive but non-functional placeholder for the chatbot.

import React from 'react';
import { Box, VStack, HStack, Input, Button, Text, Avatar, Flex } from '@chakra-ui/react';
import { PhoneIcon } from '@chakra-ui/icons';

const ChatMessage = ({ name, message, isUser }) => (
  <Flex alignSelf={isUser ? 'flex-end' : 'flex-start'}>
    {!isUser && <Avatar size="sm" name={name} mr={3} />}
    <Box
      bg={isUser ? 'teal.500' : 'gray.200'}
      color={isUser ? 'white' : 'black'}
      px={4}
      py={2}
      borderRadius="lg"
      maxW="80%"
    >
      {message}
    </Box>
  </Flex>
);

const Chatbot = () => {
  return (
    <VStack
      h="500px"
      w="100%"
      borderWidth={1}
      borderRadius="lg"
      boxShadow="lg"
      bg="white"
      p={4}
      spacing={4}
      align="stretch"
    >
      <Box flex={1} overflowY="auto" p={2}>
        <VStack spacing={4} align="stretch">
          <ChatMessage name="Savvy Bot" message="Hello! I am Savvy, your personal scheme assistant. How can I help you today?" />
          <ChatMessage name="Savvy Bot" message="You can ask me things like 'I am a 22 year old student in Gujarat'." />
          <ChatMessage isUser={true} message="I am a farmer in Vadodara." />
           <ChatMessage name="Savvy Bot" message="Great! Let me find schemes for farmers in Gujarat..." />
        </VStack>
      </Box>
      <HStack>
        <Input placeholder="Type your message here..." isDisabled />
        <Button colorScheme="teal" isDisabled leftIcon={<PhoneIcon />}>
          Voice
        </Button>
        <Button colorScheme="teal" isDisabled>Send</Button>
      </HStack>
      <Text fontSize="xs" color="gray.500" textAlign="center">
        Chat & Voice features are in active development.
      </Text>
    </VStack>
  );
};

export default Chatbot;