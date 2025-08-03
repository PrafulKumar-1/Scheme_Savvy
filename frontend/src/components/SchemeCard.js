// This component is crucial for displaying results. No changes from before,
// but included for completeness.

import React from 'react';
import {
  Box,
  Heading,
  Text,
  Tag,
  VStack,
  Collapse,
  Button,
  useDisclosure,
  HStack,
  Link as ChakraLink
} from '@chakra-ui/react';
import { ExternalLinkIcon } from '@chakra-ui/icons';
import DocumentChecklist from './DocumentChecklist';

const SchemeCard = ({ scheme }) => {
  const { isOpen, onToggle } = useDisclosure();

  return (
    <Box
      p={5}
      shadow="md"
      borderWidth="1px"
      borderRadius="lg"
      w="100%"
      bg="white"
      transition="all 0.2s ease-in-out"
      _hover={{ shadow: 'xl', transform: 'translateY(-4px)' }}
    >
      <VStack align="start" spacing={3}>
        <HStack justify="space-between" w="100%">
           <Heading fontSize="xl">{scheme.scheme_name}</Heading>
           <Tag colorScheme="teal" size="lg" variant="solid">{scheme.category}</Tag>
        </HStack>
        <Text fontSize="sm" color="gray.500">{scheme.ministry}</Text>
        <Text mt={2} color="gray.700">{scheme.description}</Text>
        <Text fontWeight="bold" color="green.600">
          Benefits: {scheme.benefits}
        </Text>
        
        <Button onClick={onToggle} size="sm" variant="outline">
          {isOpen ? 'Hide Details' : 'Show Required Documents'}
        </Button>

        <Collapse in={isOpen} animateOpacity>
          <Box mt={4} p={4} bg="gray.50" borderRadius="md" borderWidth="1px">
            <VStack align="start" spacing={4}>
               <DocumentChecklist documents={scheme.required_documents} />
               <Button
                  as={ChakraLink}
                  href={scheme.official_link}
                  isExternal
                  colorScheme="blue"
                  rightIcon={<ExternalLinkIcon />}
                >
                  Apply at Official Portal
                </Button>
            </VStack>
          </Box>
        </Collapse>
      </VStack>
    </Box>
  );
};

export default SchemeCard;